import streamlit as st
import bot

chatbot = bot.Chatbot(api_key=st.secrets["api"])
def get_text(text):
    response = chatbot.ask(text)
    return response["choices"][0]["text"]

title = st.text_input('User:')
st.write('bot:', get_text(title))