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
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    # Handle a conversation
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    print("Asking initial question")
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages)
    if response.usage_metadata is None: raise RuntimeError("Failed API request")
    if args.verbose: print(f"""User prompt: {args.user_prompt}
Prompt tokens: {response.usage_metadata.prompt_token_count}
Response tokens: {response.usage_metadata.candidates_token_count}""")
    print(f"""Response:
{response.text}
""")



if __name__ == "__main__":
    main()
