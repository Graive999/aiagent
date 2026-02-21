import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import function_map 
from call_function import call_function
from call_function import available_functions



parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="The prompt to send to the AI")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()
messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]




def main():
    print("Hello from AIAgent!")


    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)


    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt)
    )
    if response.usage_metadata is None:
        raise RuntimeError("API request failed: No usage metadata returned")


    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


    if response.function_calls:
        function_results = []
        for fc in response.function_calls:
            result_content = call_function(fc, verbose=args.verbose)
        
            if (
                not result_content.parts 
                or not result_content.parts[0].function_response
                or result_content.parts[0].function_response.response is None
            ):
                raise Exception("Invalid function response structure")
             
            function_results.append(result_content.parts[0])
        
            if args.verbose:
                print(f"-> {result_content.parts[0].function_response.response}")

    else:
        print(response.text)


if __name__ == "__main__":
    main()
