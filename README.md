# AI-Resume-Analyzer
An AI-powered Resume Analyzer that evaluates resumes against job descriptions, extracts skills, and provides structured insights using NLP and machine learning techniques.

This project demonstrates an end-to-end ML application, from document parsing and text processing to semantic similarity and a deployed web interface.

🚀 Features

📄 Resume Parsing – Extracts text from PDF resumes

🧠 Skill Extraction – Identifies technical skills using NLP

📊 Resume–Job Match Score – Semantic similarity using Sentence-BERT

🏷️ Keyword Matching – Highlights missing and matched skills

🌐 Interactive UI – Built with Streamlit for easy use

🛠️ Tech Stack

Programming Language: Python

Backend: FastAPI

Frontend: Streamlit

NLP & ML:

Sentence-Transformers (SBERT)

spaCy

scikit-learn

Data Handling: pandas, numpy

PDF Processing: pdfplumber

🧩 Project Architecture
AI-Resume-Analyzer

│
├── backend/
│   ├── main.py              # FastAPI backend
│   ├── skill_extractor.py   # Skill extraction logic
│   ├── similarity.py        # Resume–JD similarity scoring
│
├── frontend/
│   └── streamlit_app.py     # Streamlit UI
│
├── models/
│   └── sbert_model/         # Sentence-BERT model
│
├── requirements.txt
├── README.md

⚙️ How It Works

User uploads a resume (PDF) and provides a job description

Resume text is extracted and cleaned

Skills are identified using NLP techniques

Resume and job description are embedded using SBERT

A similarity score is computed to estimate job fit

Results are displayed via an interactive Streamlit dashboard

▶️ How to Run Locally

1️⃣ Clone the repository
git clone https://github.com/shifa-ml/Ai-Resume-Analyzer.git
cd ai-resume-analyzer

2️⃣ Create and activate virtual environment
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Start backend (FastAPI)
uvicorn backend.main:app --reload

5️⃣ Start frontend (Streamlit)
streamlit run frontend/streamlit_app.py

📸 Demo

<img width="1299" height="819" alt="Screenshot 2025-12-26 202503" src="https://github.com/user-attachments/assets/7c80c49a-3aae-47b4-af4b-ae8944f39c7f" />

<img width="1026" height="761" alt="Screenshot 2025-12-26 202947" src="https://github.com/user-attachments/assets/2fa52a64-e997-4e70-a913-e38babff9d4b" />

Result
<img width="967" height="654" alt="image" src="https://github.com/user-attachments/assets/d16ffaa2-1966-4665-9cd2-056fe8a8981d" />


📌 Use Cases

Students optimizing resumes for internships

Job seekers checking resume–JD alignment

Recruiters performing quick resume screening

🔮 Future Improvements

Resume section-wise scoring

ATS-friendly resume feedback

Support for multiple resumes

Deployment on cloud (AWS / GCP)

👩‍💻 Author

Shifa Ahmad
B.Tech AI & ML
Aspiring ML Engineer | Open Source Contributor
