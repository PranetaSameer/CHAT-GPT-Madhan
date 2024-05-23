 
import os
import pathlib
import textwrap
from PIL import Image
import google.generativeai as genai

from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-pro-latest')


input = 'tell me about yourself'
def get_gemini_response(input, model=genai.GenerativeModel('gemini-1.5-pro-latest')):
  response = model.generate_content(input)
  return response.text
print(get_gemini_response(input, model))