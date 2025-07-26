import os
from openai import OpenAI
from google import genai

def get_openai_client():
    return OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_gemini_client():
    return genai.Client()
