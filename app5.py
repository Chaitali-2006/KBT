import streamlit as st 

st.markdown("""
<style>
            .stButton > button 
                {
                    background-color:green;
                    color:pink;
                    border-radius:50%;
                }




""", unsafe_allow_html=True)
    


st.title("welcome to basic streamlit app")
fname = st.text_input("enter 1st name")
mname = st.text_input("enter middle name")
lname = st.text_input("enter last name")
age =st.slider("select your age",1,100)
city =st.selectbox("select youe city ",["delhi","mumbai","nashik"])

if st.button("show Details"):
    st.write("1st name:",fname)
    st.write("middle name:",mname)
    st.write("last name:",lname)
    st.write("age",age)
    st.write("city",city)

    