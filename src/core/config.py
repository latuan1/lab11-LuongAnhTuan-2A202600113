"""
Lab 11 — Configuration & API Key Setup
"""
import os
from pathlib import Path


def _load_env_file(env_path: Path) -> None:
    """Load simple KEY=VALUE pairs from a .env file into os.environ."""
    if not env_path.exists():
        return

    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")

        if key and key not in os.environ:
            os.environ[key] = value


def setup_api_key():
    """Load Google API key from the environment."""
    src_root = Path(__file__).resolve().parents[1]
    _load_env_file(src_root / ".env")

    if not os.environ.get("GOOGLE_API_KEY"):
        raise RuntimeError(
            "GOOGLE_API_KEY is not set in the environment or .env file. Set it before running the app."
        )
    os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "0"
    print("API key loaded.")


# Allowed banking topics (used by topic_filter)
ALLOWED_TOPICS = [
    "banking", "account", "transaction", "transfer",
    "loan", "interest", "savings", "credit",
    "deposit", "withdrawal", "balance", "payment",
    "tai khoan", "giao dich", "tiet kiem", "lai suat",
    "chuyen tien", "the tin dung", "so du", "vay",
    "ngan hang", "atm",
]

# Blocked topics (immediate reject)
BLOCKED_TOPICS = [
    "hack", "exploit", "weapon", "drug", "illegal",
    "violence", "gambling", "bomb", "kill", "steal",
]
