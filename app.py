import os
import streamlit as st
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA

# === Загрузка переменных из .env ===
load_dotenv()
assert "OPENAI_API_KEY" in os.environ, "OPENAI_API_KEY не найден в .env файле"

# === Пути ===
DB_PATH = "/Users/Tosha/Desktop/al-Buhari RAG application/faiss_index"

# === Инициализация моделей ===
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.load_local(
    folder_path=DB_PATH,
    embeddings=embeddings,
    allow_dangerous_deserialization=True
)
retriever = vectorstore.as_retriever()

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.0)

qa = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True
)

# === Интерфейс Streamlit ===
st.set_page_config(page_title="Ask al-Bukhari", layout="wide")
st.title("📖 Ask al-Bukhari — RAG Question Answering")

query = st.text_input("Your query:")

if query:
    with st.spinner("Searching for answer..."):
        result = qa({"query": query})

        st.markdown("### Answer:")
        st.write(result["result"])

        st.markdown("### Source Hadith(s):")
        for i, doc in enumerate(result["source_documents"], 1):
            st.markdown(f"**{i}.** {doc.page_content}")
            meta = doc.metadata
            st.markdown(f"*Volume:* `{meta.get('volume', '')}` | *Book:* `{meta.get('book', '')}` | *Number:* `{meta.get('number', '')}` | *Narrator:* `{meta.get('narrator', '')}`")
            st.markdown("---")