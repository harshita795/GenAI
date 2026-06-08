import streamlit as st

# Page configurations
st.set_page_config(page_title="My AI Projects Hub", page_icon="🚀", layout="centered")

# Main Header
st.title("🚀 My AI Project Hub")
st.write("Click on any card below to launch and test my live deep learning models.")

st.markdown("---")

# --- PROJECT 1 CARD ---
with st.container(border=True):
    st.subheader("🎬 Movie Review Sentiment Analysis (RNN)")
    st.write("An NLP web application that analyzes user reviews and classifies them as Positive or Negative using a Recurrent Neural Network.")
    
    # 🔗 REPLACE WITH YOUR ACTUAL DEPLOYED STREAMLIT URL
    rnn_link = "https://imdb--review.streamlit.app/" 
    st.link_button("👉 Launch RNN App", rnn_link, type="primary")

st.markdown(" ") # Spacer

# --- PROJECT 2 CARD ---
with st.container(border=True):
    st.subheader("📊 Customer Churn Classification (ANN)")
    st.write("A predictive application using an Artificial Neural Network to analyze tabular data profiles and evaluate customer retention probabilities.")
    
    # 🔗 REPLACE WITH YOUR ACTUAL DEPLOYED STREAMLIT URL
    ann_link = "https://my-customer-churn.streamlit.app/" 
    st.link_button("👉 Launch ANN App", ann_link, type="primary")

st.markdown("---")
st.caption("Developed by [harshita795](https://github.com) | Built with Streamlit")
