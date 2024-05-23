import google.generativeai as genai

load_dotenv()

genai.configure(api_key='AIzaSyCywxL3BTdCMWt22qmZIxpOJVECFNbr02s')
model = genai.GenerativeModel('gemini-1.5-pro-latest')


input = 'tell me about yourself'
def get_gemini_response(input, model=genai.GenerativeModel('gemini-1.5-pro-latest')):
  response = model.generate_content(input)
  return response.text
print(get_gemini_response(input, model))
