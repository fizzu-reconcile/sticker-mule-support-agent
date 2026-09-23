
import os
from openai import OpenAI


def detect_intent(message):
    message = message.lower()

    if any(word in message for word in [
    "shipping",
    "delivery",
    "delivered",
    "package",
    "parcel",
    "shipment"
]):

    if any(word in message for word in ["order", "order number", "purchase"]):
        return "order"

    if any(word in message for word in ["refund", "return", "money back"]):
        return "refund"

    if any(word in message for word in ["price", "cost", "pricing"]):
        return "pricing"

    return "general"


def support_agent(message):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    intent = detect_intent(message)

    response = client.responses.create(
        model="gpt-4o-mini",
        instructions=(
            "You are a helpful customer support agent for Sticker Mule. "
            "Answer customer questions clearly and professionally. "
            "The detected customer intent is: " + intent + ". "
            "Do not invent order information, shipping status, refunds, "
            "or company policies. If specific account information is needed, "
            "ask the customer to provide the relevant details."
        ),
        input=message
    )

    return response.output_text


if __name__ == "__main__":
    print("Sticker Mule Support Agent")

    test_message = "I have a question about my shipping"
    print(support_agent(test_message))
