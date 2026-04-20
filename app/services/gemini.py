import vertexai
from vertexai.generative_models import GenerativeModel

def call_gemini(prompt: str) -> str:
    try:
        vertexai.init(
            project="my-jee-ai-project",
            location="us-central1"
        )

        model = GenerativeModel("gemini-1.5-flash")

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:
        print(f"Gemini error: {e}")
        return "AI service is temporarily unavailable. Showing fallback explanation."