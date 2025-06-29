import google.generativeai as genai
from django.conf import settings

genai.configure(api_key=settings.GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")  

def generate_response(prompt: str) -> str:
    try:
        # for m in genai.list_models():
        #     print(m.name, m.supported_generation_methods)
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"