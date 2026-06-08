import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import load_model
import streamlit as st
import os

# Load the IMDB dataset word_index
@st.cache_resource # Keeps the app fast by loading the data only once
@st.cache_resource 
def load_assets():
    word_index = imdb.get_word_index()
    reverse_word_index = {value: key for key, value in word_index.items()}
    
    # 2. Dynamically look inside the current directory of main.py
    current_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(current_dir, "simple_rnn_imdb_model.h5")
    
    # 3. Load using the absolute path
    model = load_model(model_path)
    return reverse_word_index, word_index, model

reverse_word_index, word_index, model = load_assets()

# Function to decode reviews
def decode_reviews(encoded_review):
    return " ".join([reverse_word_index.get(i - 3, "?") for i in encoded_review])

# Function to preprocess user input
def preprocessed_text(text):
    words = text.lower().split()
    encoded_review = [word_index.get(word, 2) + 3 for word in words]
    padded_review = sequence.pad_sequences([encoded_review], maxlen=500) 
    return padded_review

# Prediction function
def predict_sentiment(review):
    preprocessed_input = preprocessed_text(review)
    prediction = model.predict(preprocessed_input)
    sentiment = "Positive" if prediction[0][0] > 0.5 else "Negative"
    return sentiment, prediction[0][0]

# Streamlit UI
st.title("IMDB Movie Review Sentiment Analysis")
st.write("Enter a movie review to classify it as positive or negative.")

user_input = st.text_area("Movie Review", placeholder="Type your review here...")

if st.button("Classify"):
    if user_input.strip(): # Check if the user actually typed words
        sentiment, score = predict_sentiment(user_input)
        
        # Make the output look clean using Streamlit metrics
        if sentiment == "Positive":
            st.success(f"**Sentiment:** {sentiment}")
        else:
            st.error(f"**Sentiment:** {sentiment}")
            
        st.info(f"**Confidence Score:** {score:.4f}")
    else:
        st.warning("Please enter a valid movie review before classifying.")
