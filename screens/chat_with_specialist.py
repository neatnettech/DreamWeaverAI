import streamlit as st
import time

def get_static_response(question_index):
    responses = [
        "Sure, I can help you with that. Here are some tips on how to improve your sleep patterns.",
        "It's important to establish a consistent sleep routine. Try going to bed and waking up at the same time every day.",
        "Avoid using electronic devices at least an hour before bed to help your mind unwind.",
        "Consider incorporating relaxation techniques like deep breathing or meditation before bed.",
        "If you continue having trouble sleeping, it might be a good idea to consult a healthcare professional."
    ]
    return responses[question_index % len(responses)]

def app():
    st.title("Chat with Specialist")

    st.write("""
    Have a question or need advice? Chat with our AI assistant.
    """)

    if "conversation" not in st.session_state:
        st.session_state.conversation = []

    input_placeholder = st.empty()

    user_input = input_placeholder.text_input("Ask your question here:")

    if user_input:
        question_index = len(st.session_state.conversation)
        ai_response = get_static_response(question_index)
        
        st.session_state.conversation.append({"question": user_input, "answer": None})
        
        input_placeholder.text_input("Ask your question here:", value="", key="empty")

        time.sleep(2)

        st.session_state.conversation[-1]["answer"] = ai_response

    for entry in st.session_state.conversation:
        st.markdown(f"**You:** {entry['question']}")
        if entry["answer"]:
            st.markdown(f"**Doe, John (MD):** {entry['answer']}")
        st.markdown("---")