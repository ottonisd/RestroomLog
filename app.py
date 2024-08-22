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
    app = TravelLogGUI()

    st.title("Classroom Travel Log GUI")

    if 'id_text' not in st.session_state:
        st.session_state.id_text = ''

    if st.session_state.id_text == '':
        id_text = st.text_input("Please scan ID and select.", key="id_text")
    else:
        id_text = st.session_state.id_text

    count_label = st.empty()

    if st.button("Restroom"):
        if id_text:
            if id_text in app.rr_list:
                app.update_log(f"Returned from restroom: {app.get_time()}", id_text)
                app.rr_list.remove(id_text)
                app.count -= 1
            else:
                app.update_log(f"Leaving to restroom: {app.get_time()}", id_text)
                app.rr_list.append(id_text)
                app.count += 1

            count_label.write(f"Out to restroom: {app.count}")
            st.session_state.id_text = ''
        else:
            st.write("Please scan ID and select.")

if __name__ == "__main__":
    main()
