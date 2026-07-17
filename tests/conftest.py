import importlib.util
from pathlib import Path

import pytest

MODULE_PATH = Path(__file__).resolve().parent.parent / "app" / "control-keyboard.py"


def _load_module():
    spec = importlib.util.spec_from_file_location("control_keyboard", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def ck(monkeypatch):
    """Load the control-keyboard module with keyboard and sleep neutralised.

    ``keyboard.send`` is replaced by a stub that records every key sent and
    ``sleep`` is turned into a no-op so tests run instantly without triggering
    real key presses.
    """
    module = _load_module()

    sent_keys = []
    monkeypatch.setattr(module.keyboard, "send", lambda key: sent_keys.append(key))
    monkeypatch.setattr(module, "sleep", lambda _seconds: None)

    module.sent_keys = sent_keys
    return module
