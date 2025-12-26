import spacy

nlp = spacy.load("en_core_web_sm")

def preprocess_text(text: str) -> str:
    """
    Clean and normalize text for NLP similarity
    """
    doc = nlp(text.lower())

    tokens = [
        token.lemma_
        for token in doc
        if not token.is_stop
        and not token.is_punct
        and token.is_alpha
    ]

    return " ".join(tokens)

