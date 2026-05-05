import os
import sys
from groq import Groq


def ask_groq(user_question: str) -> str:
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError("GROQ_API_KEY is missing. Add it in GitHub Secrets or environment variables.")

    client = Groq(api_key=api_key)

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant. Answer briefly and clearly."
            },
            {
                "role": "user",
                "content": user_question
            }
        ],
        temperature=0.3,
        max_tokens=100
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    question = " ".join(sys.argv[1:]) or "Explain GitHub Actions in one line."
    answer = ask_groq(question)

    print("Question:", question)
    print("Answer:", answer)