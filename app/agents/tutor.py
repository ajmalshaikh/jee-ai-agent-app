from services.gemini import call_gemini

def tutor_agent(topic: str):
    prompt = f"""
    You are a JEE tutor.
    Explain {topic} in simple steps for a 12th student.
    Include examples.
    """

    try:
        return call_gemini(prompt)
    except:
        return f"Here is a simple explanation of {topic}."
