import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


# 8. Use the generate_content method with the required named parameters
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
)

# 9. Print the .text property of the response object
print(response.text)

def main():
    print("Hello from aiagent!")


if __name__ == "__main__":
    main()
