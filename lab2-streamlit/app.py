import streamlit as st

# Title
st.title("🎓 Student Feedback System")

# Student Name
name = st.text_input("Enter your name:")

# Subject Selection
subject = st.selectbox(
    "Select Subject:",
    ["Mathematics", "Science", "English", "History", "Computer Science"]
)

# Rating
rating = st.slider("Rate the subject (1 = Poor, 5 = Excellent):", 1, 5, 3)

# Comments
comments = st.text_area("Additional Comments:")

# Submit Button
if st.button("Submit Feedback"):
    if name.strip() == "":
        st.error("⚠️ Please enter your name before submitting.")
    else:
        st.success("✅ Feedback Submitted Successfully!")
        
        # Display confirmation
        st.write("### 📋 Submitted Feedback")
        st.write(f"**Name:** {name}")
        st.write(f"**Subject:** {subject}")
        st.write(f"**Rating:** {rating} ⭐")
        st.write(f"**Comments:** {comments if comments.strip() else 'No comments provided.'}")
