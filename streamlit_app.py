import streamlit as st
from screens import home, generate_story, generate_noise, sleep_statistics, ai_recommendations, device_integration, today_statistics, rag_screen, chat_with_specialist

st.set_page_config(page_title="DreamWeaver AI", page_icon='💤', layout='wide')

PAGES = {
    "Home": home,
    "Today's Sleep Statistics": today_statistics,
    "Generate Story": generate_story,
    "Generate Noise": generate_noise,
    "Insights": sleep_statistics,
    "AI Recommendations": ai_recommendations,
    "Devices": device_integration,
    "Chat with Specialist": chat_with_specialist,
    "Retrieval-Augmented Generation": rag_screen
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

page = PAGES[selection]
page.app()