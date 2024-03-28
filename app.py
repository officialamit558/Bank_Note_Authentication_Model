import numpy as np
import pandas as pd
import pickle
import streamlit as st

# Load the model
model_name = open("bank_authentication_model.pkl", "rb")
load_model = pickle.load(model_name)

def welcome():
    return "Welcome User"

def predict_note_authentication(variance, skewness, curtosis, entropy):
    # Convert inputs to float
    variance = float(variance)
    skewness = float(skewness)
    curtosis = float(curtosis)
    entropy = float(entropy)
    
    # Predict using the loaded model
    prediction = load_model.predict([[variance, skewness, curtosis, entropy]])
    return prediction

def main():
    st.title("Bank Authenticator")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    variance = st.text_input("Variance", "Type Here")
    skewness = st.text_input("Skewness", "Type Here")
    curtosis = st.text_input("Curtosis", "Type Here")
    entropy = st.text_input("Entropy", "Type Here")
    result = ""
    if st.button("Predict"):
        result = predict_note_authentication(variance, skewness, curtosis, entropy)
        st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Let's Learn")
        st.text("Built with Streamlit")

if __name__ == "__main__":
    main()
