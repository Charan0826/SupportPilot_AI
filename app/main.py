from dotenv import load_dotenv
from google import genai
import os


def main():
    load_dotenv()

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        print("Error: Gemini API key not found.")
        return

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents="Explain what an AI customer support agent does in 2 simple sentences."
    )

    print("Gemini's response:")
    print(response.text)


if __name__ == "__main__":
    main()