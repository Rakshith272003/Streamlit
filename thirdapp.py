import streamlit as st

# ---- Configurations ----
st.set_page_config(page_title="My Portfolio", layout="wide")

# ---- Header Section ----
st.title("Welcome to My Portfolio! 👨‍💻")
st.subheader("Hi, I'm [Your Name], a passionate developer and learner.")

st.markdown("""
I'm skilled in:
- Web Development (React, Django, etc.)
- Data Science (Python, Pandas, Streamlit)
- Machine Learning & AI

Feel free to explore my projects below or connect with me!
""")

# ---- About Me Section ----
st.header("About Me")
st.image("images/your_photo.jpg", width=150, caption="Your Name")  # Add your photo to the `images` folder
st.write("""
I am a software engineer with a keen interest in building impactful solutions.
I enjoy working on projects that challenge my problem-solving skills and push
me to learn new technologies.
""")

# ---- Skills Section ----
st.header("Skills")
skills = {
    "Programming Languages": "Python, JavaScript, C++",
    "Frameworks": "Django, React, Streamlit",
    "Tools": "Git, Docker, AWS"
}
for skill, details in skills.items():
    st.write(f"**{skill}:** {details}")

# ---- Projects Section ----
st.header("Projects")
projects = {
    "Real-Time Whiteboard App": "A collaborative whiteboard using WebSockets and Streamlit.",
    "Traffic Management System": "An AI-powered solution to optimize traffic light timing.",
    "Gesture-Controlled Mouse": "A virtual mouse controlled by hand gestures using computer vision."
}
for project, desc in projects.items():
    st.subheader(project)
    st.write(desc)
    st.markdown("[View on GitHub](#)")  # Replace # with actual links

# ---- Contact Section ----
st.header("Contact Me")
contact_form = """
<form action="https://formsubmit.co/your_email@example.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your Name" required>
    <input type="email" name="email" placeholder="Your Email" required>
    <textarea name="message" placeholder="Your Message"></textarea>
    <button type="submit">Send</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)
