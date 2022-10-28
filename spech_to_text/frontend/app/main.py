import streamlit as st
import os
import requests

STYLES = {
    "Big_model": "model_big",
    "Smail_model": "model_smail"
}

style = st.selectbox("Choose the style", [i for i in STYLES.keys()])

# Настройка боковой панели
st.sidebar.title("About")
st.sidebar.info(
    """
    This service for recognition and processing audio to text.
    """
)
st.sidebar.info("Feel free to collaborate and comment on the work. The github link can be found "
                "https://github.com/")

st.header("Trascribe Audio, only mp3 format!")
fileObject = st.file_uploader(label="Please upload your file")

if st.button("Transcription"):
    with st.spinner('Wait for precessing:...'):
        files = {"file": fileObject.getvalue()}
        res = requests.post(f"http://178.154.240.11:8081/{style}", files=files)
        img_path = res.json()

        audio_file = open('../../backend/app/save/extract.mp3', 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio / ogg')
        audio_file.close()

        st.subheader("Trascribe result: ")
        st.markdown(img_path.get("name"))

        os.remove("../../backend/app/save/soung.mp3")
        os.remove("../../backend/app/save/extract.mp3")
    st.success('Done!')