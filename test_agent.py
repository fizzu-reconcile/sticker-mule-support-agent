from app import support_agent


def test_support_agent_exists():
    assert callable(support_agent)
