import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def support_agent(message):
    response = client.responses.create(
        model="gpt-4o-mini",
        instructions=(
            "You are a helpful customer support agent for Sticker Mule. "
            "Answer customer questions clearly and professionally. "
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
    answer = support_agent(test_message)

    print(answer)
