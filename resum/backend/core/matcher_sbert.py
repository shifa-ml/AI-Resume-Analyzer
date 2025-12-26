from sklearn.metrics.pairwise import cosine_similarity
from backend.models.sbert_model import model

def sbert_similarity(resume_text: str, jd_text: str) -> float:
    """
    Compute SBERT-based semantic similarity
    """
    resume_emb = model.encode(resume_text)
    jd_emb = model.encode(jd_text)

    score = cosine_similarity([resume_emb], [jd_emb])[0][0]
    return float(round(score * 100, 2))


