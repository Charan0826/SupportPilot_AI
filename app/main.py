
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    load_dotenv()

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        print("Error: Gemini API key not found.")
        return

    client = genai.Client(api_key=api_key)

    chat = client.chats.create(
        model="gemini-3.8-flash"
    )

    print("Welcome to SupportPilot AI!")
    print("Type 'exit' to quit.\n")

    while True:
        question = input("You: ").strip()

        if question.lower() == "exit":
            print("SupportPilot AI: Goodbye!")
            break

        if not question:
            continue

        try:
            response = chat.send_message(question)
            print("\nSupportPilot AI:", response.text, "\n")

        except Exception as error:
            print("Sorry, something went wrong.")
            print("Error:", error)


if __name__ == "__main__":
    main()
