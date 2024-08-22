import streamlit as st
from datetime import datetime


def main():
    if 'text_box' not in st.session_state:
        st.session_state.text_box = st.text_input("Enter text:")
    else:
        st.session_state.text_box = st.text_input("Enter text:", value="")

    if st.button("Clear"):
        st.session_state.text_box = st.text_input("Enter text:", value="")

if __name__ == "__main__":
    main()
