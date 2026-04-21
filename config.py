import json
import os

CONFIG_PATH = os.path.expanduser("~/.promptmol.json")

DEFAULTS = {
    "backend": "lmstudio",
    "model": "local-model",
    "api_key": "",
    "base_url": "http://localhost:1234/v1",
    "max_history": 20,
    "anthropic_model": "claude-sonnet-4-6",
    "openai_model": "gpt-4o",
    "output_dir": "",  # empty = use current working directory
}


def load_config() -> dict:
    if not os.path.exists(CONFIG_PATH):
        return dict(DEFAULTS)
    with open(CONFIG_PATH) as f:
        data = json.load(f)
    config = dict(DEFAULTS)
    config.update(data)
    return config


def save_config(key: str, value: str) -> None:
    config = load_config()
    if key in ("max_history",):
        config[key] = int(value)
    else:
        config[key] = value
    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f, indent=2)


def get(key: str):
    return load_config().get(key, DEFAULTS.get(key))
