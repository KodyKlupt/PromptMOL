import sys
from typing import Callable, Dict, List, Optional

from . import config


def chat(
    messages: List[Dict[str, str]],
    on_token: Optional[Callable[[str], None]] = None,
    model_override: Optional[str] = None,
) -> str:
    """Send messages to the configured LLM backend.

    Streams tokens via *on_token* callback as they arrive (or to stdout if
    on_token is None).  Returns the complete assembled response text.
    model_override, if given, replaces the configured model for this call only.
    """
    cfg = config.load_config()
    backend = cfg.get("backend", "lmstudio")

    if backend in ("lmstudio", "openai"):
        return _openai_chat(messages, cfg, on_token=on_token, model_override=model_override)
    elif backend == "anthropic":
        return _anthropic_chat(messages, cfg, on_token=on_token, model_override=model_override)
    elif backend == "google":
        return _google_chat(messages, cfg, on_token=on_token, model_override=model_override)
    else:
        raise RuntimeError(f"Unknown backend '{backend}'. Use: lmstudio, openai, anthropic, google")


def _emit(token: str, on_token: Optional[Callable]) -> None:
    """Write a token to the on_token callback or directly to stdout."""
    if on_token:
        on_token(token)
    else:
        sys.stdout.write(token)
        sys.stdout.flush()


def _openai_chat(
    messages: List[Dict[str, str]],
    cfg: dict,
    on_token: Optional[Callable] = None,
    model_override: Optional[str] = None,
) -> str:
    try:
        from openai import OpenAI
    except ImportError:
        raise RuntimeError("openai package not installed. Run: pip install openai")

    backend = cfg.get("backend", "lmstudio")

    if backend == "lmstudio":
        base_url = cfg.get("base_url", "http://localhost:1234/v1")
        api_key = cfg.get("api_key") or "lm-studio"
        default_model = cfg.get("model", "local-model")
    else:
        base_url = "https://api.openai.com/v1"
        api_key = cfg.get("api_key", "")
        default_model = cfg.get("openai_model", "gpt-4o")
        if not api_key:
            raise RuntimeError("OpenAI API key not set. Run: pmcfg set api_key <your-key>")

    model = model_override or default_model

    try:
        client = OpenAI(base_url=base_url, api_key=api_key)
        stream = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.1,
            max_tokens=2048,
            stream=True,
        )
        chunks: List[str] = []
        for chunk in stream:
            delta = chunk.choices[0].delta.content
            if delta:
                chunks.append(delta)
                _emit(delta, on_token)
        if not on_token:
            sys.stdout.write("\n")
            sys.stdout.flush()
        return "".join(chunks)
    except Exception as e:
        raise RuntimeError(f"LLM call failed ({backend}): {e}")


def _anthropic_chat(
    messages: List[Dict[str, str]],
    cfg: dict,
    on_token: Optional[Callable] = None,
    model_override: Optional[str] = None,
) -> str:
    try:
        import anthropic
    except ImportError:
        raise RuntimeError("anthropic package not installed. Run: pip install anthropic")

    api_key = cfg.get("api_key", "")
    if not api_key:
        raise RuntimeError("Anthropic API key not set. Run: pmcfg set api_key <your-key>")

    model = model_override or cfg.get("anthropic_model", "claude-sonnet-4-6")

    # Separate the system message — Anthropic takes it as a distinct param.
    # Wrap it with cache_control so the large system prompt is cached server-side
    # after the first call (5-min TTL), cutting latency and cost on every turn.
    system_content = ""
    filtered: List[Dict] = []
    for msg in messages:
        if msg["role"] == "system":
            system_content = msg["content"]
        else:
            filtered.append({"role": msg["role"], "content": msg["content"]})

    if not filtered:
        raise RuntimeError("No user messages to send.")

    system_param = (
        [{"type": "text", "text": system_content, "cache_control": {"type": "ephemeral"}}]
        if system_content
        else []
    )

    try:
        client = anthropic.Anthropic(api_key=api_key)
        kwargs: dict = dict(model=model, max_tokens=2048, messages=filtered)
        if system_param:
            kwargs["system"] = system_param

        full_text: List[str] = []
        with client.messages.stream(**kwargs) as stream:
            for text in stream.text_stream:
                full_text.append(text)
                _emit(text, on_token)
        if not on_token:
            sys.stdout.write("\n")
            sys.stdout.flush()
        return "".join(full_text)
    except Exception as e:
        raise RuntimeError(f"LLM call failed (anthropic): {e}")


def _google_chat(
    messages: List[Dict[str, str]],
    cfg: dict,
    on_token: Optional[Callable] = None,
    model_override: Optional[str] = None,
) -> str:
    try:
        from google import genai
        from google.genai import types as gtypes
    except ImportError:
        raise RuntimeError(
            "google-genai package not installed. Run: pip install google-genai"
        )

    api_key = cfg.get("google_api_key", "")
    if not api_key:
        raise RuntimeError(
            "Google API key not set. Run: pmcfg set google_api_key <your-key>\n"
            "Get a key at: https://aistudio.google.com/apikey"
        )

    model = model_override or cfg.get("google_model", "gemini-2.0-flash")

    # Separate system message — Google takes it as system_instruction
    system_instruction = ""
    contents: List[Dict] = []
    for msg in messages:
        if msg["role"] == "system":
            system_instruction = msg["content"]
        else:
            # Google uses "user" / "model" (not "assistant")
            role = "model" if msg["role"] == "assistant" else "user"
            contents.append({"role": role, "parts": [{"text": msg["content"]}]})

    if not contents:
        raise RuntimeError("No user messages to send.")

    gen_config = gtypes.GenerateContentConfig(
        temperature=0.1,
        max_output_tokens=2048,
        system_instruction=system_instruction or None,
    )

    try:
        client = genai.Client(api_key=api_key)
        full_text: List[str] = []
        for chunk in client.models.generate_content_stream(
            model=model,
            contents=contents,
            config=gen_config,
        ):
            if chunk.text:
                full_text.append(chunk.text)
                _emit(chunk.text, on_token)
        if not on_token:
            sys.stdout.write("\n")
            sys.stdout.flush()
        return "".join(full_text)
    except Exception as e:
        raise RuntimeError(f"LLM call failed (google): {e}")
