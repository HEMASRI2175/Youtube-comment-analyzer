from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_text_splitters import TokenTextSplitter
from langchain.chains.summarize import load_summarize_chain
from dotenv import load_dotenv
import streamlit as st

gemini_api_key = st.secrets['GEMINI_API_KEY']
load_dotenv()

def get_summary(text):
    # Validate Input
    if not text:
        raise ValueError("Input text cannot be empty or None")
    if not isinstance(text, str):
        raise TypeError(f"Expected a string, but got {type(text).__name__}")
    
    # Tokenization
    text_splitter = TokenTextSplitter(
        chunk_size=1000,
        chunk_overlap=10
    )
    try:
        chunks = text_splitter.create_documents([text])
    except Exception as e:
        raise ValueError(f"Error in text splitting: {str(e)}")

    # Summarization
    llm = ChatGoogleGenerativeAI(
        model="gemini-pro",
        google_api_key=gemini_api_key
    )
    
    chain = load_summarize_chain(
        llm,
        chain_type="map_reduce"
    )

    # Invoke Chain
    try:
        response = chain.run(chunks)
    except Exception as e:
        raise RuntimeError(f"Error in summarization chain: {str(e)}")

    return response
