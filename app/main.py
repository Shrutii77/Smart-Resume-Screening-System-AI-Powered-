import os
import json
from dotenv import load_dotenv
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import HTMLResponse
import google.generativeai as genai
from PyPDF2 import PdfReader

load_dotenv()
app = FastAPI()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-3.6-flash")

@app.get("/", response_class=HTMLResponse)
def home():
    return open("app/index.html", "r").read()

@app.post("/screen_resume")
async def screen(job_description: str = Form(...), resume_file: UploadFile = File(None), resume_text: str = Form("")):
    try:
        content = ""
        if resume_file:
            reader = PdfReader(resume_file.file)
            content = "".join([page.extract_text() or "" for page in reader.pages])
        elif resume_text:
            content = resume_text

        if not content:
            return {"error": "Please provide a resume file or text."}
        
        prompt = f"""
        Analyze this resume against the job description for a Python developer role:
        JOB DESCRIPTION: {job_description}
        RESUME: {content}

        Return output ONLY as a valid JSON object with these exact keys:
        {{
            "match_score": <number between 0 to 100>,
            "matched_skills": ["skill1", "skill2"],
            "missing_skills": ["skill1", "skill2"],
            "explanation": "Short 2-3 lines explanation"
        }}
        """
        
        response = model.generate_content(prompt)
        text_response = response.text.strip()
        
        if "```json" in text_response:
            text_response = text_response.split("```json")[1].split("```")[0].strip()
        elif "```" in text_response:
            text_response = text_response.split("```")[1].split("```")[0].strip()
            
        return json.loads(text_response)

    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)