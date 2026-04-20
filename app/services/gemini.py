import vertexai
from vertexai.generative_models import GenerativeModel

def call_gemini(prompt: str) -> str:
    try:
        vertexai.init(
            project="my-jee-ai-project",
            location="us-central1"
        )

        # ✅ Use stable model
        model = GenerativeModel("gemini-1.0-pro")

        response = model.generate_content(prompt)

        return response.text if response.text else "No response from AI"

    except Exception as e:
        print(f"Gemini FULL ERROR: {str(e)}")
        return f"Fallback triggered. Error: {str(e)}"