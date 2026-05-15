"""
Thin i18n layer — loads translations from locales/{lang}.json.
Fallback: returns the key itself when a translation is missing.
"""
import json
from pathlib import Path

_LOCALES_DIR = Path(__file__).resolve().parent / "locales"
_LANG = "en"
_STRINGS: dict[str, str] = {}


def _load_config_lang() -> str:
    """Read language preference from user config, default 'en'."""
    try:
        from constants import USER_CONFIG_FILE, DEFAULT_CONFIG
        if USER_CONFIG_FILE.exists():
            cfg = json.loads(USER_CONFIG_FILE.read_text())
            return cfg.get("lang", DEFAULT_CONFIG.get("lang", "en"))
    except Exception:
        pass
    return "en"


def set_language(lang: str) -> None:
    """Switch to a different language at runtime."""
    global _LANG, _STRINGS
    _LANG = lang
    _STRINGS = _load_file(lang)


def _load_file(lang: str) -> dict[str, str]:
    path = _LOCALES_DIR / f"{lang}.json"
    if path.exists():
        try:
            return json.loads(path.read_text())
        except (json.JSONDecodeError, OSError):
            pass
    # Fallback to English
    en_path = _LOCALES_DIR / "en.json"
    if en_path.exists() and lang != "en":
        try:
            return json.loads(en_path.read_text())
        except (json.JSONDecodeError, OSError):
            pass
    return {}


def t(key: str, **kwargs) -> str:
    """Translate a key. Unknown keys fall back to the key itself.
    Supports Python format variables: t("hello {name}", name="World")
    """
    text = _STRINGS.get(key, key)
    if kwargs:
        try:
            text = text.format(**kwargs)
        except (KeyError, ValueError):
            pass
    return text


# Auto-load on import
_LANG = _load_config_lang()
_STRINGS = _load_file(_LANG)
