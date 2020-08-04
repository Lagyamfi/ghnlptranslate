import streamlit as st
from PIL import Image
import pickle, requests

# Specify English-Twi endpoint
address = "http://paul-gpu-dev.eastus.cloudapp.azure.com:5000/" # example, when running locally

# run details
run_details = {"text input" : None,
                "translation" :None,
                "rating" : None,
                "alt translation": None}

# creating the titles and image
st.title("GhanaNLP Twi Translator")
st.header("Generate Twi translations from English")
st.info("Note: Twi output is mainly of the Akuapem Dialect")
image = Image.open("./GhanaNLP logo v2 (black).png")
st.sidebar.image(image, width=200)
test_input = st.text_input("Enter an English sentence:")
run_details['text input'] = test_input

#if st.button("Translate"):
with st.spinner("Translating..."):
    r = requests.post(address+'?in='+' '.join(test_input.split()))
    result = r.text
    run_details["translation"] = result
st.write(result)
st.text("Twi Translation: ")


@st.cache(allow_output_mutation=True)
def get_data():
    return []

#if st.button("Translate"):
#    get_data().append({"Input": test_input, "Translation": result})


add_radio  = st.radio(
    "How would you rate the translation from 1 (poor) to 5 (Excellent)?",
    list(range(1,6))
)
run_details["rating"] = add_radio

alt_translation = st.text_input("Please enter an alternative translation if applicable: ")

run_details["alt translation"] = alt_translation

print(run_details)

logger = open("output.txt", "a")
print(*list(run_details.values()), sep=",", end="\n", file=logger)
logger.close()

