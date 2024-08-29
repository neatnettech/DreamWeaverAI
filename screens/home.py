import streamlit as st

def app():
    st.title("Welcome to DreamWeaver AI")
    video_file = open("videos/DreamWeaverAILogovideo.mp4", "rb")
    video_bytes = video_file.read()
    st.video(video_bytes, format="video/mp4", start_time=0, loop=True, autoplay=True)