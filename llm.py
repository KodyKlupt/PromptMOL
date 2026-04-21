from typing import List, Dict
from . import config


def chat(messages: List[Dict[str, str]]) -> str:
    """Send messages to the configured LLM backend and return the response text."""
    cfg = config.load_config()
    backend = cfg.get("backend", "lmstudio")

    if backend in ("lmstudio", "openai"):
        return _openai_chat(messages, cfg)
    elif backend == "anthropic":
        return _anthropic_chat(messages, cfg)
    else:
        raise RuntimeError(f"Unknown backend '{backend}'. Use: lmstudio, openai, anthropic")


def _openai_chat(messages: List[Dict[str, str]], cfg: dict) -> str:
    try:
        from openai import OpenAI
    except ImportError:
        raise RuntimeError("openai package not installed. Run: pip install openai")

    backend = cfg.get("backend", "lmstudio")

    if backend == "lmstudio":
        base_url = cfg.get("base_url", "http://localhost:1234/v1")
        api_key = cfg.get("api_key") or "lm-studio"
        model = cfg.get("model", "local-model")
    else:
        base_url = "https://api.openai.com/v1"
        api_key = cfg.get("api_key", "")
        model = cfg.get("openai_model", "gpt-4o")
        if not api_key:
            raise RuntimeError("OpenAI API key not set. Run: pmcfg set api_key <your-key>")

    try:
        client = OpenAI(base_url=base_url, api_key=api_key)
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.1,
            max_tokens=2048,
        )
        return response.choices[0].message.content
    except Exception as e:
        raise RuntimeError(f"LLM call failed ({backend}): {e}")


def _anthropic_chat(messages: List[Dict[str, str]], cfg: dict) -> str:
    try:
        import anthropic
    except ImportError:
        raise RuntimeError("anthropic package not installed. Run: pip install anthropic")

    api_key = cfg.get("api_key", "")
    if not api_key:
        raise RuntimeError("Anthropic API key not set. Run: pmcfg set api_key <your-key>")

    model = cfg.get("anthropic_model", "claude-sonnet-4-6")

    # Extract system message from messages list (Anthropic uses separate system param)
    system = ""
    filtered = []
    for msg in messages:
        if msg["role"] == "system":
            system = msg["content"]
        else:
            filtered.append({"role": msg["role"], "content": msg["content"]})

    if not filtered:
        raise RuntimeError("No user messages to send.")

    try:
        client = anthropic.Anthropic(api_key=api_key)
        kwargs = dict(
            model=model,
            max_tokens=2048,
            messages=filtered,
        )
        if system:
            kwargs["system"] = system
        response = client.messages.create(**kwargs)
        return response.content[0].text
    except Exception as e:
        raise RuntimeError(f"LLM call failed (anthropic): {e}")
