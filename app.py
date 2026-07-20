import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Exam Score Predictor",
    page_icon="📚",
    layout="wide"
)

# Title
st.title("📚 Exam Score Predictor")

# Subtitle
st.write("Predict your exam score based on study hours.")

st.title("Exam Score Predictor")
st.header("Student Information")
st.subheader("Enter Details")
st.write("Welcome to the ML App")
st.success("Model Loaded Successfully")
st.warning("Study more!")
st.error("Invalid Input")
st.info("This model uses Linear Regression.")
Hours = st.number_input(
    "Study Hours",
    min_value=0,
    max_value=12,
    value=5
)
Hours = st.slider(
    "Study Hours",
    0,
    12,
    5
)
name = st.text_input("Student Name")
gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)
study = st.radio(
    "Study Type",
    ["Self Study", "Coaching"]
)
agree = st.checkbox("I Agree")
if st.button("Predict"):
   st.success("Prediction Done")
st.progress(75)
st.balloons()
st.sidebar.title("Menu")

hours = st.sidebar.slider(
    "Hours",
    0,
    12,
    5
)
col1, col2 = st.columns(2)

with col1:
    st.write("Column 1")

with col2:
    st.write("Column 2")
st.image("student.jpg", width=250)
import pandas as pd

df = pd.read_csv("dataset/student_scores.csv")

st.dataframe(df)
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.scatter(df["Hours"], df["Score"])

st.pyplot(fig)
