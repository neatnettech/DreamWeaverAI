import streamlit as st
import streamlit_scrollable_textbox as stx
from utilz.llama_response import getLLamaSleepscapeResponse
from utilz.text_to_speech import text_to_speech

def app():
    st.title("Generate a Bedtime Story or Meditation")
    
    input_text = st.text_input("Enter the Sleepscape topic 😴")
    col1, col2 = st.columns([3, 5])

    with col1:
        no_words = st.text_input('No of Words')
    with col2:
        sleepscape_type = st.selectbox('Sleepscape type', ('Bedtime story', 'Meditation'), index=0)

    if st.button("Generate"):
        with st.spinner(f'Generating {sleepscape_type}...'):
            story = getLLamaSleepscapeResponse(input_text, no_words, sleepscape_type)
            stx.scrollableTextbox(f' {story}', height=200)
        
        with st.spinner('Generating Audio...'):
            filename = f"{sleepscape_type.replace(' ', '_').lower()}.mp3"
            text_to_speech(story, filename)
            st.audio(filename, format="audio/mpeg", loop=True, autoplay=True)