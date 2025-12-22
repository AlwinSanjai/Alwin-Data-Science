import pandas as pd
import streamlit as st

# Load dataset
df = pd.read_csv("skills_dataset.csv")

st.title("Smart Resume Skill Gap Analyzer")

resume_text = st.text_area("Paste Your Resume Text")
role = st.selectbox("Select Job Role", df["role"].unique())

if st.button("Analyze"):
    role_skills = df[df["role"] == role]["skills"].values[0].split(",")

    resume_text = resume_text.lower()
    matched_skills = [skill for skill in role_skills if skill in resume_text]

    missing_skills = list(set(role_skills) - set(matched_skills))

    match_percentage = (len(matched_skills) / len(role_skills)) * 100

    st.subheader("Results")
    st.write(f"Skill Match Percentage: **{round(match_percentage,2)}%**")
    st.write("✅ Matched Skills:", matched_skills)
    st.write("❌ Missing Skills:", missing_skills)
