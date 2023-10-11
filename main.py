from dotenv import load_dotenv
import os
import openai
from llama_index import (
    VectorStoreIndex,
    Document,
    SimpleWebPageReader,
    StorageContext,
    load_index_from_storage,
)
import streamlit as st

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("Ask a web page")

uploaded_url = st.text_input("Enter a URL for static web page")

if len(uploaded_url) > 0:
    relevant_html = SimpleWebPageReader(html_to_text=True).load_data([uploaded_url])
    if len(relevant_html) > 0:
        html_content = relevant_html[0].text

        documents = [Document(text=html_content)]

        index = VectorStoreIndex.from_documents(documents)
        index.storage_context.persist()

        storage_context = StorageContext.from_defaults(persist_dir="./storage")
        index = load_index_from_storage(storage_context)

        query_engine = index.as_query_engine()

        query = st.text_input("Ask your question")

        button = st.button("Ask")

        if button:
            response = query_engine.query(query)
            st.write(response.response)
