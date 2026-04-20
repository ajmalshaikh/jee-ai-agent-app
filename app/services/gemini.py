import os
from google import genai

def call_gemini(prompt: str) -> str:
    try:
        api_key = os.environ.get("GEMINI_API_KEY")

        if not api_key:
            return "ERROR: Missing GEMINI_API_KEY"

        client = genai.Client(api_key=api_key)

        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"ERROR: {str(e)}"