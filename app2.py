import streamlit as st 

st.title("welcome to basic streamlit app")

age =st.slider("select your age",1,100)
city =st.selectbox("select youe city ",["delhi","mumbai","nashik"])

if st.button("show Details"):
    st.write("age",age)
    st.write("city",city)
    