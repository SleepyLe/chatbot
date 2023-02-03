import streamlit as st
import bot
title = st.text_input('User:')
st.write('bot:', bot.get_text(title))