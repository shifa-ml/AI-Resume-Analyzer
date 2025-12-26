import json
import re
from pathlib import Path

SKILLS_PATH = Path("backend/data/skills.json")

with open(SKILLS_PATH) as f:
    SKILLS = json.load(f)

def extract_skills(text: str):
    """
    Extract skills from text using keyword matching
    """
    text = text.lower()
    found_skills = set()

    for skill in SKILLS:
        pattern = rf"\b{re.escape(skill.lower())}\b"
        if re.search(pattern, text):
            found_skills.add(skill)

    return sorted(found_skills)

