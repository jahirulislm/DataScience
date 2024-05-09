import streamlit as st
import PyPDF2
import io
import openai
import docx2txt
import pyperclip
import os

# setting up OpenAI ApI key
openai.api_key= st.sidebar.text_input('OpenAI API Key', type='password')


# Function to extract text from PDF file
def extract_text_from_pdf(pdf_path):
    with open(pdf_path,'rb') as pdf_file:
        pdf_reader= PyPDF2.PdfReader(pdf_file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pagee[page_num]
            text += page.extract_text()
        return text
    
# list pdf files in a dicrectory
def list_pdf_files(directory):
    pdf_files = []
    for filename in os.listdir(directory):
        if filename.lower().endwith('.pdf'):
            pdf_files.append(os.path.join(directory, filename))
    return pdf_files
        