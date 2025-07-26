import os
from openai import OpenAI
from google import genai

def get_openai_client():
    return OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_gemini_client():
    return genai.Client()


class LLMClient:
    """Support only gemini for now"""
    def __init__(self, agent: str):
        if agent == "gemini":
            self.client = get_gemini_client()
        else:
            raise ValueError(f"Unsupported agent: {agent}")

    def generate(self, prompt: str, **kwargs):
        response = self.client.models.generate_content(
            contents=prompt,
            **kwargs
        )
        return response.text