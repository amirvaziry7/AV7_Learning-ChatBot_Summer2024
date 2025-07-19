"""
Chatbot Functions
"""

import streamlit as st
import chatbot_constants as constants


def set_page_config() -> None:
    st.set_page_config(page_title=constants.PAGE_TITLE, page_icon="👋", layout="wide")
    st.markdown(body=constants.STREAMLIT_STYLE, unsafe_allow_html=True)


def initial_session_state() -> None:
    if "model_name" not in st.session_state:
        st.session_state.model_name = constants.MODELS[0]

    if "messages" not in st.session_state:
        st.session_state.messages = [constants.SYSTEM_MESSAGE]


def get_assistant_answer(user_prompt: str) -> str:
    assistant_answer = f"متاسفانه من پاسخ سوال شما را نمی‌دانم! {user_prompt}"
    return assistant_answer

# def get_assistant_answer(model_name: str, messages: list, temperature: float = 0.8) -> str:
#     pass