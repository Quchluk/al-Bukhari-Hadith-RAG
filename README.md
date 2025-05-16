# 🕌 al-Bukhari Hadith RAG

A Retrieval-Augmented Generation (RAG) application that answers natural-language questions based on **Sahih al-Bukhari**. Built with LangChain, OpenAI models, and FAISS, using Streamlit for the interface.

---

## 🚀 Features

* Search over **7,000+ normalized hadiths** from Sahih al-Bukhari
* Uses **FAISS vector search** with OpenAI Embeddings
* Real-time **Q\&A interface** in your browser via Streamlit
* Source metadata shown: volume, book, narrator, number
* Reproducible pipeline for building your own index from raw data

---

## 🧱 Repository Structure

```
al-bukhari-rag/
├── app.py                         # Streamlit app
├── build_index.py                # Build FAISS index from normalized data
├── faiss_index/                  # Prebuilt FAISS index (optional or downloadable)
├── Data/
│   └── sahih_bukhari_normalized.jsonl
├── preprocessing/
│   ├── normalize_hadiths.py      # Normalizes raw data into flat JSONL
│   └── README.md                 # Explanation of preprocessing steps
├── requirements.txt
├── .env.example                  # Environment variable template
├── .gitignore
├── LICENSE
└── README.md                     # This file
```

---

## 📦 Installation

```bash
git clone git@github.com:Quchluk/al-Bukhari-Hadith-RAG.git
cd al-Bukhari-Hadith-RAG
pip install -r requirements.txt
```

---

## 🔐 API Key Setup

1. Copy `.env.example` to `.env`:

```bash
cp .env.example .env
```

2. Add your OpenAI API key:

```
OPENAI_API_KEY=sk-...
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🧠 Using the Prebuilt Index

This repo may include a prebuilt FAISS index (`faiss_index/`) or you can download it separately via GitHub Releases.

If you'd rather build it yourself or switch embedding models, see below.

---

## 🛠 Rebuilding the Index from Raw Data

All normalization and indexing steps are provided.

```bash
# (Optional) Normalize raw JSON into flat JSONL
python preprocessing/normalize_hadiths.py \
  --input Data/sahih_bukhari_raw.json \
  --output Data/sahih_bukhari_normalized.jsonl

# Build FAISS index
python build_index.py
```

> ⚠️ When using a prebuilt FAISS index, make sure to include `allow_dangerous_deserialization=True` when loading, since FAISS uses pickle.

---

## 📚 Data Sources

Hadiths were adapted from open-source Bukhari datasets. Index structure and code are original.

Raw data was sourced from [essaji/Complete-Sahih-Bukhari-Json](https://github.com/essaji/Complete-Sahih-Bukhari-Json) — big thanks to the author for providing the original JSON structure.

---

## 📄 License

This project is licensed under the **MIT License**. See the `LICENSE` file for full terms.

---

## 👤 Author

Built by [Anton Smirnov](https://github.com/Quchluk)

Use this in your portfolio, fork it, build on it — all welcome!
