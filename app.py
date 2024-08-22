import streamlit as st
from datetime import datetime

class TravelLogGUI:
    def __init__(self):
        self.count = 0
        self.rr_list = []

    def update_log(self, message, id_text):
        with open("RRLog.txt", "a") as log_file:
            log_file.write(f"{id_text}  {message}\n")
        st.write(message)

    def get_time(self):
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def main():
    text_box = st.text_input("Enter text:")
    if st.button("Clear"):
        st.session_state.text_box = ""

if __name__ == "__main__":
    main()
