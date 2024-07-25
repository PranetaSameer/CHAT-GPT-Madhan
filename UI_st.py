import streamlit as st
from models import get_gemini_response, get_gemini_response_image, yt_summerize, imagegen
from PIL import Image
import io



##initialize our streamlit app

st.set_page_config(page_title="BOT GPT")
st.header("PROFILE BOT")

col1, col2, col3 = st.columns(3)
with col1:
    st.button("Chat with host tables")

input=st.text_area("Input Prompt: ",key="input")
    
submit=st.button("submit")

response = ''
## If ask button is clicked
yt ="https://www.youtube.com"
list = ["create image", "generate image", "create picture", "generate picture"]
contains_keyword = any(keyword in input.lower() for keyword in list)

