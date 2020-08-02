import streamlit as st
from PIL import Image
import pickle, requests

# Specify English-Twi endpoint
address = "http://paul-gpu-dev.eastus.cloudapp.azure.com:5000/" # example, when running locally

# creating the titles and image
st.title("GhanaNLP Twi Translator")
st.header("Generate Twi translations from English")
image = Image.open("./GhanaNLP logo v2 (black).png")
st.image(image, width=200)
test_input = st.text_input("Enter an English sentence:")
st.text("Twi Translation: ")
with st.spinner("Translating..."):
    r = requests.post(address+'?in='+' '.join(test_input.split()))
    result = r.text
st.write(result)