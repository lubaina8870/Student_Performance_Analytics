
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(
    page_title="Student Performance Dashboard",
    page_icon="📊",
    layout="wide"
)

# Dashboard title
st.title("📊 Student Performance Analytics Dashboard")
st.write("Analyze student marks and academic performance.")

# Load dataset
df = pd.read_csv("students.csv")

# Calculate total and average
subjects = ["Maths", "Science", "English", "Computer"]

df["Total"] = df[subjects].sum(axis=1)
df["Average"] = df[subjects].mean(axis=1)

# Pass or fail
df["Result"] = df["Average"].apply(
    lambda x: "Pass" if x >= 50 else "Fail"
)

# Dashboard metrics
st.subheader("Overall Performance")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Students", len(df))
col2.metric("Average Marks", round(df["Average"].mean(), 2))
col3.metric("Highest Average", round(df["Average"].max(), 2))
col4.metric(
    "Pass Percentage",
    f"{(df['Result'].eq('Pass').mean() * 100):.1f}%"
)

# Student data table
st.subheader("Student Details")
st.dataframe(df, use_container_width=True)

# Subject-wise average
st.subheader("Subject-wise Average Marks")

subject_average = df[subjects].mean()

fig, ax = plt.subplots()
subject_average.plot(kind="bar", ax=ax)

ax.set_xlabel("Subjects")
ax.set_ylabel("Average Marks")
ax.set_ylim(0, 100)
ax.set_title("Average Marks by Subject")

st.pyplot(fig)
plt.close(fig)

# Student performance chart
st.subheader("Individual Student Performance")

student_names = df["Name"].tolist()

selected_student = st.selectbox(
    "Select a student",
    student_names
)

student_data = df[df["Name"] == selected_student].iloc[0]

st.write("Student Name:", selected_student)
st.write("Total Marks:", student_data["Total"])
st.write("Average Marks:", round(student_data["Average"], 2))
st.write("Result:", student_data["Result"])

# Footer
st.caption("Student Performance Analytics | Python Project")
