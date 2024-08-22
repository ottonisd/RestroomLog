import streamlit as st

placeholder = st.empty()

input = placeholder.text_input('Enter a number:', key=1)
click_clear = st.button('Clear', key=3)
if click_clear:
    message = f"{input} has left"
    st.write(message)
    placeholder.empty()
    input = placeholder.text_input('Enter a number:', value='', key=2)
    input  # This line is important to update the input variable
