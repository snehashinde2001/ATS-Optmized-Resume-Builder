# ats_api.py
import requests

def get_ats_score(resume_text):
    """
    Send resume text to a free ATS scoring API.
    Replace 'https://free-ats-api.com/score' with actual API endpoint.
    """
    try:
        response = requests.post(
            "https://free-ats-api.com/score",
            json={"resume": resume_text}
        )
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Failed to fetch ATS score"}
    except Exception as e:
        return {"error": str(e)}
