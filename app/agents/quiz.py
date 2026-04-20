from services.gemini import call_gemini

def quiz_agent(topic: str):
    prompt = f"""
    Generate 3 JEE-level MCQs on {topic}.
    Provide answers and explanations in JSON format.
    """

    try:
        response = call_gemini(prompt)
        return response
    except:
        return [
            {"question": f"What is {topic}?", "answer": "Fallback", "explanation": "Fallback explanation"}
        ]
