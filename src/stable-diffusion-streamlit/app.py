import streamlit as st
import os

app_title = os.environ.get("APP_TITLE", "Streamlit, Stable Diffusion online image generation tool")
st.title(app_title)
body = """+ [Text to Image](./Text to Image)
+ [gallery](./gallery)
"""
st.markdown(body, unsafe_allow_html=False)
