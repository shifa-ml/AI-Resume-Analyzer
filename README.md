# AI-Resume-Analyzer
An AI-powered Resume Analyzer that evaluates resumes against job descriptions, extracts skills, and provides structured insights using NLP and machine learning techniques.

This project demonstrates an end-to-end ML application, from document parsing and text processing to semantic similarity and a deployed web interface.

 Features

   Resume Parsing – Extracts text from PDF resumes

   Skill Extraction – Identifies technical skills using NLP

   Resume–Job Match Score – Semantic similarity using Sentence-BERT

   Keyword Matching – Highlights missing and matched skills

   Interactive UI – Built with Streamlit for easy use

   Tech Stack

Programming Language: Python

Backend: FastAPI

Frontend: Streamlit

NLP & ML:

Sentence-Transformers (SBERT)

spaCy

scikit-learn

Data Handling: pandas, numpy

PDF Processing: pdfplumber

Project Architecture

AI-Resume-Analyzer

│
├── backend/
│   ├── app.py                  # FastAPI entry point
│   ├── api/
│   │   └── routes.py            # API endpoints
│   ├── core/
│   │   ├── pdf_parser.py        # PDF → text
│   │   ├── preprocess.py        # Cleaning & NLP
│   │   ├── skill_extractor.py   # Skill matching
│   │   ├── matcher.py           # TF-IDF / SBERT logic
│   │
│   ├── models/
│   │   └── sbert_model.py       # Load SBERT model
│   │
│   ├── data/
│   │   └── skills.json          # Skill dictionary
│   │
│   └── requirements.txt
│
├── frontend/
│   └── streamlit_app.py         # UI
│
├── sample_data/
│   ├── resume.pdf
│   └── job_description.txt
│
├── README.md
├── .gitignore
└── run.sh


 How It Works

User uploads a resume (PDF) and provides a job description

Resume text is extracted and cleaned

Skills are identified using NLP techniques

Resume and job description are embedded using SBERT

A similarity score is computed to estimate job fit

Results are displayed via an interactive Streamlit dashboard

 How to Run Locally

1 Clone the repository
git clone https://github.com/shifa-ml/Ai-Resume-Analyzer.git
cd ai-resume-analyzer

2 Create and activate virtual environment
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows

3 Install dependencies
pip install -r requirements.txt

4 Start backend (FastAPI)
uvicorn backend.main:app --reload

5 Start frontend (Streamlit)
streamlit run frontend/streamlit_app.py

 Demo

<img width="1299" height="819" alt="Screenshot 2025-12-26 202503" src="https://github.com/user-attachments/assets/7c80c49a-3aae-47b4-af4b-ae8944f39c7f" />

<img width="1026" height="761" alt="Screenshot 2025-12-26 202947" src="https://github.com/user-attachments/assets/2fa52a64-e997-4e70-a913-e38babff9d4b" />

Result
<img width="967" height="654" alt="image" src="https://github.com/user-attachments/assets/d16ffaa2-1966-4665-9cd2-056fe8a8981d" />


 Use Cases

Students optimizing resumes for internships

Job seekers checking resume–JD alignment

Recruiters performing quick resume screening

👩‍💻 Author

Shifa Ahmad
B.Tech AI & ML
Aspiring ML Engineer | Open Source Contributor
