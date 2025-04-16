import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")  # or hardcode your key

def get_resume_feedback(resume_text, jd_text):
    prompt = f"Given this resume:\n\n{resume_text}\n\nAnd this job description:\n\n{jd_text}\n\nGive feedback to improve the resume."
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']