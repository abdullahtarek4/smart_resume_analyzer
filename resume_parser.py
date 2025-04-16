import re
import spacy
from pdfminer.high_level import extract_text

nlp=spacy.load('en_core_web_sm')

def extract_resume_text(file):
    return extract_text(file)

def extract_email(text):
    match=re.search(r'[\w\.-]+@[\w\.-]+',text)
    return match.group(0) if match else None

def extract_skills(text,skill_list):
    skills_found=[]
    text=text.lower()
    for skill in skill_list:
        if skill.lower() in text:
            skills_found.append(skill)
    return list(set(skills_found))  

def extract_phone(text):
    match=re.search(r'\+?\d[\d -]{8,}\d',text)
    return match.group(0) if match else None