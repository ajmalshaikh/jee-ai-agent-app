from app.services.gemini import call_gemini

def quiz_agent(topic):
    prompt = f"""
    Generate 5 JEE-level MCQs on {topic}.
    Provide answers and explanations.
    """
    return call_gemini(prompt)