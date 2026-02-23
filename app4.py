import streamlit as st

st.title("Simple chatbot")

Q =st.text_input("ask me anything")
if st.button("send"):
    st.write("question",Q)
    st.write("reply soon")