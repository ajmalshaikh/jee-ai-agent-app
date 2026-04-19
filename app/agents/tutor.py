# ✅ correct
from services.gemini import call_gemini

def tutor_agent(topic):
    prompt = f"""
    You are a JEE tutor.
    Explain {topic} in simple steps for a 12th student.
    Include examples.
    """
    return call_gemini(prompt)
