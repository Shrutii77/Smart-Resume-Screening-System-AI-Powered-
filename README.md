# Smart-Resume-Screening-System (AI-Powered)
​An intelligent, full-stack recruitment tool built for the AI/ML Developer evaluation. This application leverages the power of Large Language Models (Google Gemini) via FastAPI and provides a sleek, modern UI built with Tailwind CSS to instantly screen resumes against specific job descriptions.
 
# ​🚀 Key Features
​
**Dual Resume Input Support:** Upload resumes as .pdf files (parsed automatically via PyPDF2) or paste raw resume text directly.


​**LLM-Powered Matching Logic:** Uses Google's generative AI to perform deep contextual semantic matching rather than simple keyword counting.

​
**Structured JSON Output:** Guarantees precise extraction of match scores, matched skills, missing skills, and a concise explanation.

​
**Modern Glassmorphism UI:** Responsive frontend built using Tailwind CSS with a clean split-screen layout powered by Vanilla JavaScript.


# 🛠️ Tech Stack
**>Backend:** Python, FastAPI, Uvicorn

**​>AI/ML:** Google Generative AI (google-generativeai), PyPDF2

​**>Frontend:** HTML5, Tailwind CSS, Vanilla JavaScript
​
**>Environment Management:** python-dotenv


​# ⚙️ Setup & Installation Steps
​Follow these steps to set up and run the project locally on your machine:

1. Clone the Repository
git clone (https://github.com/Shrutii77/Smart-Resume-Screening-System-AI-Powered-.git)
cd smart-resume-screening

2. Create and Activate a Virtual Environment
python -m venv venv

**On Windows:**
venv\Scripts\activate

**On macOS/Linux:**
source venv/bin/activate

1. Install Dependencies
pip install fastapi uvicorn google-generativeai python-dotenv PyPDF2

2. Configure Environment Variables
Create a .env file in the root directory of your project and add your Gemini API key:
GEMINI_API_KEY=your_actual_gemini_api_key_here

3. Project Directory Structure
Ensure your project files are structured correctly:
smart-resume-screening/

├── app/

│     └── index.html      # Frontend interface (HTML + Tailwind + Vanilla JS)

├     └── main.py             # FastAPI application backend

├── .env                # API Keys configuration

└── README.md           # Project Documentation


# 🏃‍♂️ How to Run the Application
1. Start the FastAPI server using uvicorn:
python main.py

2. (Alternatively: uvicorn main:app --reload)
Open your web browser and navigate to:
​http://127.0.0.1:8000

3. Using the App:
   
​~ Enter or paste the target Job Description.

~ ​Upload a candidate's PDF resume OR paste the resume text into the text area.

~ ​Click "Screen Resume" to view the real-time match score, skill breakdown, and AI explanation.


# 🧠 Approach & Architecture Explanation
​
1. Extraction Layer: When a request hits the /screen_resume endpoint, the system checks whether a PDF file or raw text was submitted. If a PDF is uploaded, PyPDF2 extracts all text content page by page.
​
2. Generative Intelligence: Instead of traditional rigid NLP pipelines, we utilize Google Gemini, which excels at contextual understanding. The prompt engineering explicitly instructs the model to act as a recruiter matching candidate competencies against job expectations.

3. ​Structured Response Contract: The prompt mandates a strict JSON layout containing match_score, matched_skills, missing_skills, and an explanation. The backend safely parses this structure (cleaning up markdown code blocks if present) to return a reliable dictionary to the frontend.

4. ​User Experience: The frontend uses Vanilla JavaScript (fetch API and FormData) to asynchronously submit data and dynamically render evaluation results without refreshing the page.


**​# 📸 Deliverables & Screenshots**
​Instructions for Screenshots:

1. ​Create a folder named screenshots inside your project root directory.

2. ​Save your UI screenshot as ui_screenshot.png and terminal/output screenshot as backend_output.png inside that folder.


​1. Frontend UI Design

(Dashboard where users input job descriptions and upload/paste resumes)

<img width="959" height="505" alt="1 5" src="https://github.com/user-attachments/assets/d5ac9f68-96fc-4da4-a7d2-0acadc60c04b" />


<img width="948" height="503" alt="3 7" src="https://github.com/user-attachments/assets/101748d8-250a-4065-b219-7f92a160de70" />




​2. Backend Code & API Output

**Output**
<img width="959" height="497" alt="4 7" src="https://github.com/user-attachments/assets/0aab8227-9457-422c-abbf-a5717609f338" />

**Backend Code**
<img width="959" height="503" alt="code 5" src="https://github.com/user-attachments/assets/49c6afd6-9661-4dda-8fd9-8a563513abd7" />

**Frontend Code**
<img width="959" height="502" alt="code 6 5" src="https://github.com/user-attachments/assets/50f767e7-ff63-465e-a2d9-b461017d250d" />
