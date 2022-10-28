import streamlit as st
from vosk import Model, KaldiRecognizer, SetLogLevel
from pydub import AudioSegment
import json
import os

import requests

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

if st.button("File Transfer"):
    #if image is not None and style is not None:
    files = {"file": fileObject.getvalue()}
    res = requests.post(f"http://178.154.240.11:8081/upload", files=files)
    img_path = res.json()
    if img_path != None:
        st.text("File upload to back- OK! Processing.....")
        st.text(img_path.get("name"))