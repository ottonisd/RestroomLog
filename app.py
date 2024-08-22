import streamlit as st

placeholder = st.empty()

input = placeholder.text_input('text', key=1)
click_clear = st.button('clear text input', key=3)
if click_clear:
    placeholder.empty()  # Clear the previous widget
    input = placeholder.text_input('text', value='', key=2)

st.write(input)
