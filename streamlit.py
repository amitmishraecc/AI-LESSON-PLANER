import os
import bcrypt
import pymongo
import streamlit as st

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

# --- MongoDB Connection ---
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["StudentDB"]
users = db["users"]
# 
# --- LLM Setup ---
def LLM_Setup(prompt):
    model = ChatGroq(
        model="llama-3.3-70b-versatile",
        groq_api_key=os.getenv('key')
    )
    parser = StrOutputParser()
    output = model | parser
    output = output.invoke(prompt)
    return output

# --- Streamlit Config ---
st.set_page_config(page_title="AI Lesson Planner", layout="wide")

# --- Dark / Light Mode Toggle ---
mode = st.sidebar.radio("Theme Mode", ["Light Mode", "Dark Mode"])
dark_mode = mode == "Dark Mode"

# --- Define colors based on mode ---
bg_color = "#1f2937" if dark_mode else "#f0f4f8"
text_color = "#f0f4f8" if dark_mode else "#1f2937"
card_bg_color = "#2c2c2c" if dark_mode else "#ffffff"
input_bg_color = "#3a3a3a" if dark_mode else "#ffffff"
input_text_color = "#f0f4f8" if dark_mode else "#000000" # Explicitly black for light mode inputs
button_color = "#6a11cb" if dark_mode else "#2575fc"
button_text_color = "#ffffff"

# --- Page Header ---
st.markdown(
    f"<h1 style='text-align: center; color: {button_color}; font-weight:bold;'>📚 AI Lesson Planner</h1>",
    unsafe_allow_html=True
)

# --- Session State for Login ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = None

# --- Login / Signup Section ---
if not st.session_state.logged_in:
    choice = st.sidebar.radio("Choose Action", ["Login", "Signup"])

    # Center the login/signup forms
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if choice == "Signup":
            st.markdown(
                f"<div style='background-color: {card_bg_color}; padding: 20px; border-radius: 10px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); margin-bottom: 20px;'>"
                f"<h3 style='color: {text_color}; text-align: center;'>Sign Up</h3>",
                unsafe_allow_html=True
            )
            # Use 'label_visibility="visible"' to ensure labels are always shown
            username = st.text_input("Username", key="signup_username", label_visibility="visible")
            password = st.text_input("Password", type="password", key="signup_password", label_visibility="visible")
            if st.button("Create Account", key="create_account_btn"):
                if not username or not password:
                    st.warning("⚠️ Please fill all fields")
                elif users.find_one({"username": username}):
                    st.error("⚠️ Username already exists. Try another.")
                else:
                    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
                    users.insert_one({"username": username, "password": hashed})
                    st.success("✅ Account created! Please login.")
            st.markdown("</div>", unsafe_allow_html=True)

        elif choice == "Login":
            st.markdown(
                f"<div style='background-color: {card_bg_color}; padding: 20px; border-radius: 10px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); margin-bottom: 20px;'>"
                f"<h3 style='color: {text_color}; text-align: center;'>Login</h3>",
                unsafe_allow_html=True
            )
            # Use 'label_visibility="visible"' to ensure labels are always shown
            username = st.text_input("Username", key="login_username", label_visibility="visible")
            password = st.text_input("Password", type="password", key="login_password", label_visibility="visible")
            if st.button("Login", key="login_btn"):
                user = users.find_one({"username": username})
                if user and bcrypt.checkpw(password.encode('utf-8'), user["password"]):
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.success(f"✅ Welcome, {username}!")
                    st.rerun() # Use st.rerun() for updated Streamlit versions
                else:
                    st.error("❌ Invalid credentials")
            st.markdown("</div>", unsafe_allow_html=True)

# --- AI Lesson Planner Section (Only if logged in) ---
if st.session_state.logged_in:
    st.sidebar.success(f"👤 Logged in as {st.session_state.username}")
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = None
        st.rerun() # Use st.rerun()

    st.write("---")
    st.markdown(
        f"<p style='text-align: center; font-size: 16px; color: gray;'>Generate interactive and detailed lesson plans for your students</p>",
        unsafe_allow_html=True
    )

    # Sidebar Inputs
    with st.sidebar:
        st.header("Lesson Details")
        subject = st.text_input('Subject', key="subject")
        topic = st.text_input('Topic', key="topic")
        grade = st.text_input('Grade', key="grade")
        duration = st.text_input('Duration', key="duration")
        learning_objectives = st.text_area('Learning Objectives', key="learning_objectives")
        customization = st.text_area('Customization', key="customization")

    llm_output = ""

    # Center the generate button
    col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])
    with col_btn2:
        if st.button('Generate Lesson Plan'):
            if not subject or not topic or not grade or not duration or not learning_objectives:
                st.warning('⚠️ Please fill out all required fields before generating the lesson plan.')
            else:
                with st.spinner("🧠 Generating lesson plan..."):
                    prompt = (
                        f"Generate a detailed lesson plan for the subject of {subject} on the topic of {topic}. "
                        f"This lesson is intended for {grade} students and will last for {duration}. "
                        f"The following are the learning objectives: {learning_objectives}. "
                        f"This is how the user wants the plan to be customized: {customization}. "
                        f"Return the results as Markdown."
                    )
                    llm_output = LLM_Setup(prompt)

                st.success("✅ Lesson Plan Generated!")
                st.markdown(llm_output, unsafe_allow_html=True)

# --- CSS Styling ---
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {bg_color};
        color: {text_color};
    }}

    /* Input boxes */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {{
        background-color: {input_bg_color};
        color: {input_text_color};
        font-size: 13px !important;
        border-radius: 6px !important;
        padding: 5px 10px !important;
        width: 100% !important; /* Make inputs take full width of their container */
        # max-width: 250px; /* Set a specific max-width for the input fields */
        margin: 0 auto; /* Center inputs within their container */
        display: block; /* Important for margin auto to work */
    }}

    /* Adjust label color for light mode */
    .stTextInput label, .stTextArea label {{
        color: {input_text_color}; /* Ensure labels are visible in light mode */
        font-weight: bold;
        display: block; /* Make labels block for better spacing */
        text-align: center; /* Center labels */
        margin-bottom: 5px; /* Add some space below labels */
    }}
    
    /* Specific styling for the 'subheader' of login/signup to ensure visibility */
    h3 {{
        color: {text_color};
    }}

    /* Buttons */
    div.stButton>button {{
        background: linear-gradient(90deg, #6a11cb, #2575fc);
        color: white;
        font-weight: 600;
        border-radius: 6px;
        height: 36px !important;
        width: 200px !important;
        font-size: 13px !important;
        display: block; /* Make button a block element */
        margin-left: 50%; /* Center horizontally */
        margin-right: 100%; /* Center horizontally */
        margin-top: 15px; /* Add margin above the button to separate from input */
    }}
    div.stButton>button:hover {{
        opacity: 0.9;
        transform: scale(1.03);
        transition: all 0.2s ease;
    }}

    /* For centering elements within the col2 of the login/signup section */
    .st-emotion-cache-nahz7x {{ /* This class might change with Streamlit updates, but targets the column content */
        display: flex;
        flex-direction: column;
        align-items: center;
    }}
    </style>
    """,
    unsafe_allow_html=True
)