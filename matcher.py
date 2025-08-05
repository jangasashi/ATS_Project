# matcher.py

from parser import extract_text_from_pdf
from utils import calculate_similarity

def match_resume_to_job(resume_path, jd_path):
    try:
        resume_text = extract_text_from_pdf(resume_path)
        jd_text = extract_text_from_pdf(jd_path)
        similarity = calculate_similarity(resume_text, jd_text)
        return round(similarity * 100, 2)
    except Exception as e:
        print(f"[ERROR] Failed to match resume and JD: {e}")
        return 0