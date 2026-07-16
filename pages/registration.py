import streamlit as st
from database.mongodb import students_collection
st.title("Student Registration")
firstname = st.text_input("First Name")
lastname = st.text_input("Last Name")
email = st.text_input("Email")
course = st.text_input("Course")

if st.button ("Register"):
    students_collection.insert_one({
        "firstname": firstname,
        "lastname": lastname,
        "email": email,
        "course": course
    })



st.success("student registered successfully")