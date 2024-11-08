# Importing the required libraries
import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv() # This will load the local environment vars...
import pandas as pd

# Set up the Gemini API key in VSCode
genai.configure(api_key = os.getenv("GOOGLE-API-KEY"))

# Streamlit Page
st.header("👨‍⚕️Healthcare :blue[Advisor] ⚕️", divider = "green")
input = st.text_input("Hi! I am your Medical Expert💊. Ask me Anything...")
submit = st.button("Submit")

# Create a BMI Calculator - sidebar
st.sidebar.subheader("BMI Calculator✍️")
weight = st.sidebar.text_input("Weight (in kgs):") # capture info in text
height = st.sidebar.text_input("Height (in cms):")
# BMI = Weight/height**2
height_nums = pd.to_numeric(height)
weight_nums = pd.to_numeric(weight)
height_mts = height_nums/100
bmi = weight_nums/(height_mts)**2

# BMI Scale
notes = f'''The BMI Value can be interpreted as:
* Underweight: BMI<18.5
* Normal Weight: BMI 18.5-24.9
* Overweight: BMI 25 - 29.9
* Obesity: BMI>=30'''

if bmi:
    st.sidebar.markdown("The BMI Is: ")
    st.sidebar.write(bmi)
    st.sidebar.write(notes)

# Generative AI Application

def get_response(text):
    model = genai.GenerativeModel("gemini-pro")
    if text!="":
        response = model.generate_content(text)
        return(response.text)
    else:
        st.write("Please enter Prompt!!")
    
if submit:
    response = get_response(input)
    st.subheader("The :orange[Response] is: ")
    st.write(response)

# Disclaimer
st.subheader("Disclaimer: ", divider = True)
notes = f'''
1. This is an advisor providing guidance and should not be construced as Medical Advice.
2. Before taking any action, it is be recommended to consult a Doctor.'''
st.markdown(notes)