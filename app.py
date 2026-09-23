
import os

def support_agent(message):
    """Simple AI support-agent prototype for Sticker Mule."""

    message = message.lower()

    if "shipping" in message or "delivery" in message:
        return (
            "I can help with shipping and delivery questions. "
            "Please provide your order details so the support team can check the latest status."
        )

    if "order" in message:
        return (
            "I can help with your order. "
            "Please provide your order number and the details of your request."
        )

    if "refund" in message or "return" in message:
        return (
            "I can help with refund or return questions. "
            "Please provide your order details so the request can be reviewed."
        )

    if "price" in message or "cost" in message:
        return (
            "I can help with product pricing. "
            "Please tell me which Sticker Mule product you are interested in."
        )

    return (
        "Thanks for contacting Sticker Mule Support. "
        "Please provide a few more details about your question so I can help."
    )


if __name__ == "__main__":
    print("Sticker Mule Support Agent")
    print(support_agent("I have a question about my shipping"))
