import streamlit as st
import joblib

# Load model and vectorizer
model = joblib.load("fake_news_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

st.title("Fake News Detection App")
st.markdown("Enter a news headline or article content below to check whether it's **Fake** or **Real**.")

# Text input
user_input = st.text_area("Enter news text here:")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter some text to analyze.")
    else:
        # Transform and predict
        X_input = vectorizer.transform([user_input])
        prediction = model.predict(X_input)[0]
        
        # Display result
        label = "🟢 Real News" if prediction == 1 else "🔴 Fake News"
        st.subheader("Prediction Result:")
        st.success(label)
