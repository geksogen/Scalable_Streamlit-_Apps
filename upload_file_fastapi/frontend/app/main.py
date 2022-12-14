import requests
import streamlit as st

STYLES = {
    "candy": "candy",
    "composition 6": "composition_vii",
    "feathers": "feathers",
    "la_muse": "la_muse",
    "mosaic": "mosaic",
    "starry night": "starry_night",
    "the scream": "the_scream",
    "the wave": "the_wave",
    "udnie": "udnie",
}

# https://discuss.streamlit.io/t/version-0-64-0-deprecation-warning-for-st-file-uploader-decoding/4465
st.set_option("deprecation.showfileUploaderEncoding", False)

# defines an h1 header
st.title("File transfer web app")

# displays a file uploader widget
image = st.file_uploader("Choose an file")

# displays the select widget for the styles
#style = st.selectbox("Choose the style", [i for i in STYLES.keys()])

# displays a button
if st.button("File Transfer"):
    #if image is not None and style is not None:
    files = {"file": image.getvalue()}
    res = requests.post(f"http://51.250.66.35:8081/upload", files=files)
    img_path = res.json()
    if img_path != None:
        st.text("File upload to back- OK!")
        #st.text(img_path)
