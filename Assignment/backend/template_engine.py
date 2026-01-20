# template_engine.py
import os

def apply_template(template_name, resume_data):
    """
    Replace placeholders in LaTeX template with resume data.
    """
    template_path = os.path.join("templates", template_name)
    with open(template_path, "r") as f:
        template = f.read()

    # Replace placeholders
    template = template.replace("<NAME>", resume_data["personal_info"].get("name", ""))
    template = template.replace("<EMAIL>", resume_data["personal_info"].get("email", ""))
    template = template.replace("<PHONE>", resume_data["personal_info"].get("phone", ""))
    template = template.replace("<LINKEDIN>", resume_data["personal_info"].get("linkedin", ""))

    template = template.replace("<EDUCATION>", "\n".join(resume_data.get("education", [])))
    template = template.replace("<SKILLS>", ", ".join(resume_data.get("skills", [])))
    template = template.replace("<EXPERIENCE>", "\n".join([exp["description"] for exp in resume_data.get("experience", [])]))
    template = template.replace("<PROJECTS>", "\n".join(resume_data.get("projects", [])))

    return template
