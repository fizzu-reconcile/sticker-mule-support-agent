from app import detect_intent


def test_shipping_intent():
    assert detect_intent("Where is my package?") == "shipping"


def test_delivery_intent():
    assert detect_intent("When will my order be delivered?") == "shipping"


def test_order_intent():
    assert detect_intent("I need help with my order") == "order"


def test_refund_intent():
    assert detect_intent("I want a refund") == "refund"


def test_return_intent():
    assert detect_intent("How do I return this?") == "refund"


def test_pricing_intent():
    assert detect_intent("How much does this cost?") == "pricing"


def test_general_intent():
    assert detect_intent("I have a question") == "general"
