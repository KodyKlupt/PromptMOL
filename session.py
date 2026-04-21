import datetime
from typing import List, Dict, Optional


class ConversationSession:
    def __init__(self, max_history: int = 20):
        self._messages: List[Dict[str, str]] = []
        self.max_history = max_history
        self._log: List[Dict] = []  # never trimmed — full session record
        self.started_at: str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def add_user(self, text: str) -> None:
        self._messages.append({"role": "user", "content": text})
        self._trim()

    def add_assistant(self, text: str) -> None:
        self._messages.append({"role": "assistant", "content": text})
        self._trim()

    def log_exchange(self, prompt: str, summary: str, code: Optional[str]) -> None:
        self._log.append({
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "prompt": prompt,
            "summary": summary,
            "code": code,
        })

    def get_log(self) -> List[Dict]:
        return list(self._log)

    def get_messages(self) -> List[Dict[str, str]]:
        return list(self._messages)

    def clear(self) -> None:
        self._messages.clear()
        self._log.clear()
        self.started_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def _trim(self) -> None:
        limit = self.max_history * 2
        if len(self._messages) > limit:
            self._messages = self._messages[-limit:]

    def __len__(self) -> int:
        return len(self._messages)


# Module-level singleton
_session: ConversationSession = ConversationSession()


def get_session() -> ConversationSession:
    return _session


def reset_session() -> None:
    _session.clear()


def update_max_history(n: int) -> None:
    _session.max_history = n
