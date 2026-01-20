# ai_enhancer.py
import openai

# Configure your OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

def enhance_resume(resume_text, job_description=""):
    """
    Enhance resume content using OpenAI GPT.
    Optionally optimize for a given job description.
    """
    prompt = f"""
    Improve the following resume text for ATS optimization:
    Resume: {resume_text}
    Target Job Description: {job_description}
    Enhance grammar, phrasing, keywords, and professional tone.
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )
        return response.choices[0].message["content"]
    except Exception as e:
        return f"Error: {str(e)}"
