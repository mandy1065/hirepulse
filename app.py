import streamlit as st
from data import jobs, applications
from utils import create_job, apply_to_job

st.set_page_config(page_title="HirePulse Live", layout="wide")
st.title("💼 HirePulse Live")

role = st.sidebar.selectbox("Who are you?", ["Recruiter", "Candidate"])

if role == "Recruiter":
    st.header("📢 Post a Job")
    title = st.text_input("Job Title")
    description = st.text_area("Job Description")
    skills = st.text_input("Required Skills (comma-separated)")
    location = st.text_input("Location")

    if st.button("Post Job"):
        job = create_job(title, description, skills, location)
        jobs.append(job)
        st.success("Job posted!")

    st.header("📥 Applications")
    for job in jobs:
        st.subheader(f"{job['title']} — {job['location']}")
        st.write(job['description'])
        st.write(f"Skills: {', '.join(job['skills'])}")
        job_apps = applications.get(job['id'], [])
        for app in job_apps:
            st.write(f"**{app['name']}** applied")
            st.write(f"💬 Message: {app['message']}")
            st.write(f"📎 Resume: {app['resume']}")
            if not app["chat_started"]:
                if st.button(f"Start Chat with {app['name']} for {job['title']}"):
                    app["chat_started"] = True
                    st.success(f"Chat started with {app['name']}!")
            else:
                st.info(f"Chat already started with {app['name']}")
            st.markdown("---")

elif role == "Candidate":
    st.header("📝 Apply to a Job")
    for job in jobs:
        st.subheader(f"{job['title']} — {job['location']}")
        st.write(job['description'])
        st.write(f"Skills: {', '.join(job['skills'])}")

        with st.expander(f"Apply to {job['title']}"):
            name = st.text_input(f"Your Name for {job['title']}", key=f"name_{job['id']}")
            message = st.text_area("Why are you interested?", key=f"msg_{job['id']}")
            resume = st.file_uploader("Upload Resume", type=["pdf", "doc", "docx"], key=f"resume_{job['id']}")

            if st.button("Submit Application", key=f"apply_{job['id']}"):
                apply_to_job(job['id'], name, message, resume)
                st.success("Application submitted!")
