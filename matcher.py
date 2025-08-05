from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def match_resume_to_job(resume_path, job_description_text):
    resume_text = extract_text_from_pdf(resume_path)

    documents = [resume_text, job_description_text]
    tfidf = TfidfVectorizer().fit_transform(documents)
    similarity = cosine_similarity(tfidf[0:1], tfidf[1:2])
    score = round(float(similarity[0][0]) * 100, 2)
    return score

