import streamlit as st
from PIL import Image
import google.generativeai as genai

# ---------- Configuration ----------
st.set_page_config(page_title="Gemini Chatbot", layout="centered")
GEMINI_IMAGE_PATH = "gemini_avatar.png"  # Use your uploaded image here

# ---------- API Key Input ----------
api_key = "AIzaSyA84cMkSiy9i7Ph7UJmjJSrGcpd99dAQYc"


if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.0-flash')

    st.title("🤖 My Chatbot")

    # ---------- Session State ----------
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # ---------- User Input ----------
    user_input = st.text_input("You:", placeholder="Ask something...")

    if user_input:
        # Show user message immediately
        st.session_state.chat_history.append(("You", user_input))
        st.markdown(f"**🧑‍💼 You:** {user_input}")

        # Show Gemini spinner and process reply
        with st.spinner(" Beautiful is thinking..."):
            try:
                response = model.generate_content(user_input)
                reply = response.text
            except Exception as e:
                reply = f"Error: {e}"

        st.session_state.chat_history.append(("Gemini", reply))

    # ---------- Chat History Display ----------
    st.markdown("---")
    for speaker, message in reversed(st.session_state.chat_history):
        if speaker == "You":
            st.markdown(f"**🧑‍💼 {speaker}:** {message}")
        else:
            col1, col2 = st.columns([1, 8])
            with col1:
                st.image(Image.open(GEMINI_IMAGE_PATH), width=60)
            with col2:
                st.markdown(f"**🤖 {speaker}:** {message}")
