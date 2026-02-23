import streamlit as st 

st.title("basic calculator")

num1 =int(st.number_input("enter 1st no ",step=1,format="%d"))
num2 =int(st.number_input("enter 2nd no ",step=1,format="%d"))

operation =st.selectbox("choose opration",["add","sub","mul","div"])

if st.button("calculate"):
    if operation == "add":
        st.write(num1+num2)

    elif operation == "sub":
        st.write(num1-num2)
    elif operation == "mul":
        st.write(num1*num2)
    elif operation == "div":
        if num2!=0:
            st.write(num1/num2)
        else:
            st.write("cannot div by 0")


        

