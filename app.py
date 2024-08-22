import streamlit as st

if 'text_input_value' not in st.session_state:
    st.session_state.text_input_value = ''

placeholder = st.empty()

input = placeholder.text_input('text', value=st.session_state.text_input_value, key=1)
click_clear = st.button('clear text input', key=3)
if click_clear:
    st.session_state.text_input_value = ''

st.write(input)
