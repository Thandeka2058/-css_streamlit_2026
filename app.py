import streamlit as st
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
import json
import os
from PIL import Image

st.set_page_config(layout="wide")
def load_lottie_url(path_or_url):
    try:
        s = str(path_or_url)
        if s.lower().startswith(("http://", "https://")):
            r = requests.get(s, timeout=5)
            if r.status_code != 200:
                return None
            return r.json()
        else:
            if not os.path.exists(s):
                return None
            with open(s, "r", encoding="utf-8") as f:
                return json.load(f)
    except (requests.RequestException, ValueError, json.JSONDecodeError):
        return None

# use a raw string for the local path
lottie_ani = load_lottie_url(r"C:\Users\Administrator\OneDrive - University of the Western Cape\Documents\CHPC\streamlit_files\Project\Animation\Data analytics techniques.json")
lottie_contact = load_lottie_url(r"C:\Users\Administrator\OneDrive - University of the Western Cape\Documents\CHPC\streamlit_files\Project\Animation\contact.json")
image = Image.open("Animation/IT-Infrastructure-Project-Management-Methodology.jpg")



st.write("##")
st.subheader("Hey Guys! :wave:  ")
st.write("Process Excellence Analyst | Tech Enthusiast")
st.write("""
I'm a dedicated professional with a passion for leveraging technology to drive process improvements and enhance operational efficiency.
""")
st.write('----')

with st.container():
    selected = option_menu(
        menu_title=None,
        options=["About Me", "Projects", "Contact Me"],
        icons=("person","code-slash","chat-left-text-fill"),
        orientation="horizontal",
    )
    
    if selected == 'About Me':
        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                st.write("##")
                st.subheader("I am Thandeka Ngwenya")
                st.title("Process Excellence Analyst | Tech Enthusiast")
            with col2:
                if lottie_ani:
                    st_lottie(lottie_ani)
                else:
                    st.write("Animation not available")

        st.write('----')
        with st.container():
            col3,col4 = st.columns(2)
            with col3:
                st.subheader("Education")
                st.markdown("""
                - Bachelor of Commerce in Information Systems and Economics
                - Bachelor of Commerce Honours in Information Systems
                """)
            with col4:
                st.subheader("Experience")
                st.markdown("""
                - Data Science Intern at Gijima
                - Process Excellence Analyst at Teleperformance
                """)
                st.write("""
                Passionate about transforming business processes through data-driven insights and innovative solutions. 
                I combine analytical expertise with technical acumen to deliver measurable results and drive organizational excellence.

                With a strong foundation in Information Systems and Economics, I've developed a keen ability to identify inefficiencies 
                and implement strategic improvements that enhance operational performance. My experience spans across data analysis, 
                process optimization, and IT infrastructure management.

                I'm committed to leveraging technology as a catalyst for change, helping organizations streamline their workflows and 
                achieve sustainable growth. Whether it's analyzing customer feedback, optimizing operations, or implementing digital 
                solutions, I bring a results-driven approach to every project.

                Let's collaborate and create meaningful impact together!
                """)
    if selected =="Projects":
        with st.container():
            st.header("My Projects")
            st.write("##")
            col5, col6 = st.columns((1,2))
            with col5:
                st.image(image)
            with col6:
                st.markdown("""
                - **Data Analysis on Customer Feedback**: Analyzed customer feedback data to identify key areas for service improvement.
                - **Process Optimization for Operations**: Implemented process improvements that led to a 15% increase in efficiency.
                """)
                st.markdown("[View More Projects](https://github.com/Thandeka2058/)")
    if selected =="Contact Me":
        st.header("Get in Touch!")
        st.write("##")

        contact_form = """
        <form action="https://formsubmit.co/thandekangwenya76@gmail.com" method="POST">
         <input type="text" name="name" placeholder="Your Name" required style="width:100%; padding:10px; margin:5px 0;">
         <input type="email" name="email" placeholder="Your Email" required style="width:100%; padding:10px; margin:5px 0;">
         <textarea name="message" placeholder="Message" required style="width:100%; padding:10px; margin:5px 0; height:150px;"></textarea>
         <button type="submit" style="width:100%; padding:10px; background-color:#4CAF50; color:white; border:none; cursor:pointer;">Send</button>
        </form> 
         
        """
        left_col, right_col = st.columns((2,1))
        with left_col:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_col:
            st_lottie(lottie_contact, height=300)




