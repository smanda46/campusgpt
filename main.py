import streamlit as st
from google.oauth2 import service_account
import vertexai
from vertexai.preview.generative_models import GenerativeModel

creds = service_account.Credentials.from_service_account_file("service_account.json")
vertexai.init(project="YOUR_PROJECT_ID", location="us-central1", credentials=creds)

model = GenerativeModel("gemini-2.0-flash-001")

st.set_page_config(page_title="CampusGPT", page_icon="🎓")
st.title("CampusGPT: Ask ASU AI Agent")

with open("faqs.txt", "r") as f:
    faq_context = f.read()

user_question = st.text_input("Ask me anything about ASU:")

if st.button("Ask") and user_question:
    prompt = f"""
You are an AI assistant trained on the following ASU FAQs:

{faq_context}

User question: {user_question}
Answer:
"""
    response = model.generate_content(prompt)
    st.success(response.text.strip())
