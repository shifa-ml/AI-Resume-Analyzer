from fastapi import APIRouter, UploadFile, File, Form
from backend.core.pdf_parser import extract_text_from_pdf
from backend.core.preprocess import preprocess_text
from backend.core.matcher_tfidf import tfidf_similarity
from backend.core.matcher_sbert import sbert_similarity
from backend.core.skill_extractor import extract_skills

router = APIRouter()

@router.post("/analyze")
async def analyze_resume(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    resume_text = extract_text_from_pdf(resume.file)

    resume_clean = preprocess_text(resume_text)
    jd_clean = preprocess_text(job_description)

    tfidf_score = tfidf_similarity(resume_clean, jd_clean)
    sbert_score = sbert_similarity(resume_clean, jd_clean)

    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(job_description)

    matched_skills = sorted(set(resume_skills) & set(jd_skills))
    missing_skills = sorted(set(jd_skills) - set(resume_skills))

    return {
        "tfidf_match_score": tfidf_score,
        "sbert_match_score": sbert_score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }



