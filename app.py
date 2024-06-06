from dotenv import load_dotenv

load_dotenv()

import os
import streamlit
from PIL import Image
import google.generativeai as genai
import streamlit as st
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))    



def get_gemini_response(input, image, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content(input, image=image, prompt=prompt)
    return response.text

def imput_image_setup(upload_file):
    if upload_file is not None:
        bytes_data = upload_file.getvalue()
        image_parts = [{
            "mime_type": upload_file.type,
            "data": bytes_data
        }]
        
        return image_parts
    else:
        raise FileNotFoundError("Couldn't find image in filesystem")

st.set_page_config(page_title="Invoice Extractor")    
st.title("Image Upload Example")
st.header("Gemini Application")
input = st.text_input("input Prompt: ", key="input")
    
upload_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if upload_file is not None:
    # Open the image file
    image = Image.open(upload_file)
    # Display the image
    st.image(image, caption='Uploaded Image.', use_column_width=True)

submit = st.button("Tell me about the invoice")

input_prompt = """
You are an expert in understanding invoices. You will recieve input images as invoices and you will have to answer questions based on the input image."""



if submit:
    image_parts = imput_image_setup(upload_file)
    response = get_gemini_response(input, image_parts, input_prompt)
    st.subheader("the response is")    
    st.write(response)