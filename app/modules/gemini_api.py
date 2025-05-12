# app/modules/gemini_api.py

import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("❌ GEMINI_API_KEY 환경변수가 설정되지 않았습니다.")

genai.configure(api_key=api_key)

def call_gemini(prompt: str) -> str:
    try:
        model = genai.GenerativeModel(model_name="models/gemini-pro")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"[오류 발생] {e}"
