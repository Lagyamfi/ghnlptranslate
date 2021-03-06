import streamlit as st
from PIL import Image
import joblib
import torch
from transformers import AutoTokenizer, AutoModelWithLMHead

# load model and tokenizer
#loaded_model = joblib.load("./model.pkl")
#loaded_tokenizer = joblib.load("./tokenizer.pkl")


@st.cache(suppress_st_warning=True, persist=True, show_spinner=False)
def get_models():
    tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-tw")
    model = AutoModelWithLMHead.from_pretrained("Helsinki-NLP/opus-mt-en-tw")
    return tokenizer, model

loaded_tokenizer, loaded_model = get_models()

def translate(input_word='', model=loaded_model, tokenizer=loaded_tokenizer):
    inputs = tokenizer.encode(input_word, return_tensors="pt")
    outputs = model.generate(inputs, max_length=40, num_beams=4, early_stopping=True)
    decoded_output = [tokenizer.convert_ids_to_tokens(int(outputs[0][i])) for i in range(len(outputs[0]))]
    decoded_output_string = ""
    for i in range(1,len(decoded_output)):
        decoded_output_string=decoded_output_string+decoded_output[i]
    decoded_output_string = ' '.join(decoded_output_string.strip("▁").split("▁"))
    return decoded_output_string



# creating the titles and image
st.title("GhanaNLP Twi Translator")

st.header("Generate Twi translations from English")

image = Image.open("./GhanaNLP logo v2 (black).png")

st.image(image, width=200)

test_input = st.text_input("Enter an English sentence:")

st.text("Twi Translation: ")

with st.spinner("Translating..."):
    translation = translate(test_input, loaded_model, loaded_tokenizer)



st.write(translation)



