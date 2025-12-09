import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    print("Initialising AI Agent")
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("No API key found")
    client = genai.Client(api_key=api_key)

    # Allow for user input
    parser = argparse.ArgumentParser(description="AI Agent")
    parser.add_argument("prompt", type=str, help="User prompt")
    args = parser.parse_args()

    # Handle a conversation
    messages = [type.Content(role='user', parts=[types.Part(text=args.user+prompt)])]

    print("Asking initial question")
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages)
    if response.usage_metadata is None: raise RuntimeError("Failed API request")
    print(f"""
User prompt: {args.prompt}
Prompt tokens: {response.usage_metadata.prompt_token_count}
Response tokens: {response.usage_metadata.candidates_token_count}
Response:
{response.text}
""")



if __name__ == "__main__":
    main()
