import json
import os
from langchain.docstore.document import Document
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

# .env and API KEY
load_dotenv()
assert "OPENAI_API_KEY" in os.environ, "OPENAI_API_KEY not found in environment."

#input and putput
INPUT_FILE = "sahih_bukhari_normalized.json"
OUTPUT_DIR = "project folder/faiss_index"

#Load of hadith
def load_documents(path):
    docs = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            entry = json.loads(line)
            text = entry["text"].strip()
            metadata = entry["metadata"]
            docs.append(Document(page_content=text, metadata=metadata))
    return docs

#main function
def main():
    print(f" Loading from {INPUT_FILE}...")
    docs = load_documents(INPUT_FILE)

    print(f" Vectorization {len(docs)} hadith (1 hadith = 1 chunk)...")
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(docs, embeddings)

    print(f" Saving index in {OUTPUT_DIR}...")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    vectorstore.save_local(OUTPUT_DIR)

    print("Index is done")

if __name__ == "__main__":
    main()
