import uuid

def create_job(title, description, skills, location):
    return {
        "id": str(uuid.uuid4()),
        "title": title,
        "description": description,
        "skills": [s.strip().lower() for s in skills.split(",")],
        "location": location
    }

def apply_to_job(job_id, name, message, resume):
    app = {
        "name": name,
        "message": message,
        "resume": resume.name if resume else "No file",
        "chat_started": False
    }
    if job_id in applications:
        applications[job_id].append(app)
    else:
        applications[job_id] = [app]
