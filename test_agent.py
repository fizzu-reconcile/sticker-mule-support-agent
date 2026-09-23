from app import support_agent


def test_support_agent_exists():
    assert callable(support_agent)


def test_support_agent_accepts_message():
    assert support_agent.__code__.co_argcount == 1
