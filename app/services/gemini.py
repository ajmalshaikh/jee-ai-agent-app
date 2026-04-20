import os
from google import genai

def call_gemini(prompt: str) -> str:
    try:
        client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )

        return response.text if response.text else "No response from AI"

    except Exception as e:
        print(f"Gemini FULL ERROR: {str(e)}")
        return f"Fallback triggered. Error: {str(e)}"