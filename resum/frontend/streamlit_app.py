import streamlit as st
import requests

st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

st.title("📄 AI Resume Analyzer & Job Matcher")
st.write("Upload a resume and compare it against a job description.")

# Inputs
resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste Job Description", height=180)

if st.button("Analyze"):
    if resume_file and job_description.strip():
        with st.spinner("Analyzing resume..."):
            response = requests.post(
                "http://127.0.0.1:8000/analyze",
                files={"resume": resume_file},
                data={"job_description": job_description}
            )

        if response.status_code == 200:
            result = response.json()

            st.success("Analysis Complete")

            col1, col2 = st.columns(2)
            with col1:
                st.metric("SBERT Match Score", f"{result['sbert_match_score']}%")
            with col2:
                st.metric("TF-IDF Match Score", f"{result['tfidf_match_score']}%")

            st.subheader("✅ Matched Skills")
            if result["matched_skills"]:
                st.write(", ".join(result["matched_skills"]))
            else:
                st.write("None")

            st.subheader("❌ Missing Skills")
            if result["missing_skills"]:
                st.write(", ".join(result["missing_skills"]))
            else:
                st.write("None 🎉")

        else:
            st.error("Backend error. Is FastAPI running?")
    else:
        st.warning("Please upload a resume and enter a job description.")

