import pdfplumber

def extract_text_from_pdf(file):
    """
    Extract text from a PDF file-like object
    """
    text = ""

    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + " "

    return text.strip()

