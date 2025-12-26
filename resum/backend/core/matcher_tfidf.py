from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def tfidf_similarity(resume_text: str, jd_text: str) -> float:
    """
    Compute TF-IDF cosine similarity between resume and job description
    """
    vectorizer = TfidfVectorizer()

    tfidf_matrix = vectorizer.fit_transform([resume_text, jd_text])
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

    return float(round(similarity[0][0] * 100, 2))


