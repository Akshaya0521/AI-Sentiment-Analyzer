import streamlit as st
from textblob import TextBlob

st.title("🧠 AI Sentiment Analyzer")
st.write("Enter text below and see if it's positive, negative, or neutral!")

# Text input
user_input = st.text_area("Your Text", "")

# Analyze button
if st.button("Analyze"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        analysis = TextBlob(user_input)
        polarity = analysis.sentiment.polarity

        # Determine sentiment
        if polarity > 0:
            sentiment = "😊 Positive"
        elif polarity < 0:
            sentiment = "😠 Negative"
        else:
            sentiment = "😐 Neutral"

        st.success(f"Sentiment: **{sentiment}**")
