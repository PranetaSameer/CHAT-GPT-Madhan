import streamlit as st
from models import get_gemini_response, get_gemini_response_image, yt_summerize
from PIL import Image


##initialize our streamlit app

st.set_page_config(page_title="BOT GPT")

st.header("Bot Application")
input=st.text_area("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    
submit=st.button("submit")

response = ''
## If ask button is clicked
yt ="https://www.youtube.com"
if submit:
    if yt in input:
        response = yt_summerize(input)
    st.subheader("Key Points from the video")
    st.write(response)
    else:    
        if image != "":
            response = get_gemini_response_image(input, image)
        else:
            response = get_gemini_response(input)
        st.subheader("Responses:")
        st.write(response)
