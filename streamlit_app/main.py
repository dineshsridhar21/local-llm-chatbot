# streamlit_app/main.py
import sys
import os
import streamlit as st  

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.query_pdf import ask_question

st.title("Chat with your PDF")

query = st.text_input("Ask a question about the PDF:")

if query:
    with st.spinner("Thinking..."):
        answer = ask_question(query)
        st.success(answer)

        # Optional: Log to CSV
        with open("data/chat_logs.csv", "a") as f:
            f.write(f"{query},{answer}\n")

