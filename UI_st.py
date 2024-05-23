import streamlit as st
from models import get_gemini_response
##initialize our streamlit app

st.set_page_config(page_title="Gemini Image Demo")

st.header("Bot GPT")
input=st.text_input("Input Prompt: ",key="input")

submit=st.button("submit")

## If ask button is clicked

if submit:
    responses = get_gemini_response(input)
    st.subheader("Responses:")
    st.write(responses)
