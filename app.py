import streamlit as st

st.set_page_config(page_title="FAQ Chatbot")

st.title("FAQ Chatbot")
st.write("Ask your questions below.")

faq = {
    "what is python": "Python is a popular programming language.",
    "what is ai": "AI stands for Artificial Intelligence.",
    "what is machine learning": "Machine Learning is a branch of AI.",
    "who developed python": "Python was developed by Guido van Rossum.",
    "what is streamlit": "Streamlit is a Python framework for building web apps."
}

user_question = st.text_input("Enter your question:")

if st.button("Get Answer"):
    question = user_question.lower()

    if question in faq:
        st.success(faq[question])
    else:
        st.error("Sorry, I don't know the answer to that question.")
