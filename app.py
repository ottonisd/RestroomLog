import streamlit as st

def main():
    if 'text_box' not in st.session_state:
        st.session_state.text_box = st.text_input("Enter text:", key="text_box_1")
    else:
        st.session_state.text_box = st.text_input("Enter text:", value="", key="text_box_2")

    if st.button("Clear"):
        st.session_state.text_box = st.text_input("Enter text:", value="", key="text_box_3")

if __name__ == "__main__":
    main()
