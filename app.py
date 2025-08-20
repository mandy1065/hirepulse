import streamlit as st
from data import job_seekers, online_status
from utils import filter_seekers

st.set_page_config(page_title="HirePulse", layout="wide")
st.title("🚀 HirePulse")
st.subheader("Recruiter-first hiring dashboard")

role = st.sidebar.selectbox("Who are you?", ["Job Seeker", "Recruiter"])

if role == "Job Seeker":
    st.header("🎯 Create Your Profile")
    name = st.text_input("Name")
    skills = st.text_input("Skills (comma-separated)")
    location = st.text_input("Location")
    urgency = st.selectbox("Urgency Level", ["Actively looking", "Open to offers", "Casually exploring"])
    motivation = st.text_area("Why are you looking for a job?")
    bio = st.text_area("Mini Bio (280 characters max)")
    is_online = st.checkbox("I'm Online")

    if st.button("Submit Profile"):
        profile = {
            "name": name,
            "skills": [s.strip().lower() for s in skills.split(",")],
            "location": location,
            "urgency": urgency,
            "motivation": motivation,
            "bio": bio
        }
        job_seekers.append(profile)
        online_status[name] = is_online
        st.success("Profile submitted!")

elif role == "Recruiter":
    st.header("🕵️ Browse Candidates")
    skill_filter = st.text_input("Filter by skill")
    location_filter = st.text_input("Filter by location")
    urgency_filter = st.selectbox("Filter by urgency", ["All", "Actively looking", "Open to offers", "Casually exploring"])

    filtered = filter_seekers(skill_filter, location_filter, urgency_filter, job_seekers, online_status)

    for seeker in filtered:
        st.write(f"**{seeker['name']}** — {seeker['location']}")
        st.write(f"🧠 Skills: {', '.join(seeker['skills'])}")
        st.write(f"🔥 Urgency: {seeker['urgency']}")
        st.write(f"💬 Motivation: {seeker['motivation']}")
        st.write(f"📝 Bio: {seeker['bio']}")
        if st.button(f"Ping {seeker['name']}"):
            st.success(f"You pinged {seeker['name']}!")
        st.markdown("---")
