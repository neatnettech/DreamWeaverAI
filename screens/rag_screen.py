import streamlit as st
from utilz.pdf_extraction import list_available_pdfs, extract_text_from_pdf
import google.generativeai as genai
from utilz.llama_response import get_rag_response

def app():
    st.title("Retrieval-Augmented Generation (RAG)")

    st.write("Select a PDF document from the list and ask questions to generate augmented responses based on the content of the document.")

    pdf_files = list_available_pdfs()
    selected_pdf = st.selectbox("Choose a PDF", pdf_files)
    
    if selected_pdf:
        extracted_text = extract_text_from_pdf(selected_pdf)
        st.success(f"Text extracted from {selected_pdf} successfully!")

        query = st.text_input("Ask a question based on the content of the document")
        
        if st.button("Generate Response"):
            if query:
                with st.spinner("Generating your response..."):
                    response = get_rag_response(query, extracted_text)
                st.write("### Generated Response")
                st.write(response)
            else:
                st.warning("Please enter a query.")