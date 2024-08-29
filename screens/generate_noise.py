import streamlit as st
from utilz.generate_noise import generate_white_noise, generate_natural_noise
from utilz.find_sound import find_sound

def app():
    st.title("Generate White Noise or Natural Sound")

    col1, col2 = st.columns([3, 5])

    with col1:
        noise_type = st.selectbox('Noise type', ('White noise', 'Natural noise'), index=0)
    with col2:
        duration = st.slider('Duration (seconds)', min_value=10, max_value=300, value=60)

    input_text = st.text_input("Enter sound description (for natural noise)")

    if st.button("Generate"):
        if noise_type == "White noise":
            with st.spinner("Generating White Noise Audio..."):
                generate_white_noise(duration, "white_noise.wav")
                st.audio("white_noise.wav", format="audio/wav", loop=True, autoplay=True)
        else:
            with st.spinner("Generating Natural Noise Audio..."):
                natural_sound = find_sound(input_text)
                st.audio(natural_sound, format="audio/wav", loop=True, autoplay=True)