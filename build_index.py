import json
import os
from langchain.docstore.document import Document
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

# === Загрузка .env и API ключа ===
load_dotenv()
assert "OPENAI_API_KEY" in os.environ, "OPENAI_API_KEY not found in environment."

# === Настройки ===
INPUT_FILE = "/Users/Tosha/Desktop/al-Buhari RAG application/Data/sahih_bukhari_normalized.json"
OUTPUT_DIR = "/Users/Tosha/Desktop/al-Buhari RAG application/faiss_index"

# === Загрузка хадисов ===
def load_documents(path):
    docs = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            entry = json.loads(line)
            text = entry["text"].strip()
            metadata = entry["metadata"]
            docs.append(Document(page_content=text, metadata=metadata))
    return docs

# ====== ГЛАВНАЯ ФУНКЦИЯ ======
def main():
    print(f" Загрузка хадисов из {INPUT_FILE}...")
    docs = load_documents(INPUT_FILE)

    print(f" Векторизация {len(docs)} хадисов (1 хадис = 1 чанк)...")
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(docs, embeddings)

    print(f" Сохраняю индекс в {OUTPUT_DIR}...")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    vectorstore.save_local(OUTPUT_DIR)

    print(" Индекс готов!")

# ====== ЗАПУСК ======
if __name__ == "__main__":
    main()