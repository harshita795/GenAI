import streamlit as st
import pandas as pd

st.title("Streamlit Text input")

name = st.text_input("Enter your name:")

age = st.slider("Select your age:", 0, 90, 25)

st.write(f"{name} your age is {age}")

options = ["Python", "Java", "C++", "Javascript"]
choice = st.selectbox("Choose your favourite language:", options)
st.write(f"{name} your fav lang is {choice}")

if name:
  st.write(f"{name} you are very much Beautiful.")


data = {
  "Name": ["John", "Jane", "Jake", "Jill"],
  "Age": [28, 24, 35, 40],
  "City" : ["New York", "Los Angeles", "Chicago", "Houston"]
}
  
df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

uploaded_file = st.file_uploader("Choose a CSV file", type = "csv")

if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.write(df)