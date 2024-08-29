import streamlit as st
from utilz.llama_response import get_ai_response
def app():
    st.title("Chat with Specialist")

    st.write("""
    Have a question or need advice? Chat with our AI assistant powered by Google Generative AI.
    """)

    # Maintain the conversation history
    if "conversation" not in st.session_state:
        st.session_state.conversation = []

    # Create a placeholder for the input text box
    input_placeholder = st.empty()

    # User input text box within the placeholder
    user_input = input_placeholder.text_input("Ask your question here:")

    if user_input:
        # Get AI response
        with st.spinner("AI is thinking..."):
            ai_response = get_ai_response(user_input)
        
        # Add user input and AI response to conversation
        st.session_state.conversation.append({"question": user_input, "answer": ai_response})
        
        # Clear the input box after sending by re-rendering the placeholder
        input_placeholder.text_input("Ask your question here:", value="", key="empty")

    # Display conversation history in a chat-like format
    for entry in st.session_state.conversation:
        st.markdown(f"**You:** {entry['question']}")
        st.markdown(f"**AI:** {entry['answer']}")
        st.markdown("---")