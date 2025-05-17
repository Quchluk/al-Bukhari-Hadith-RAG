# 🕌 al-Bukhari Hadith RAG

A Retrieval-Augmented Generation (RAG) application that answers natural-language questions based on **Sahih al-Bukhari**.
Built with **LangChain**, **OpenAI embeddings**, **FAISS vector search**, and **Streamlit**.

> ⚡️ Ideal for multilingual and domain-specific retrieval tasks in Digital Humanities and Islamic NLP.

<p align="center">
  <img src="assets/demo.png" alt="Streamlit demo screenshot" width="80%">
</p>

---

## 🚀 Features

* ✅ **7,000+ normalized hadiths** from Sahih al-Bukhari
* 🔎 **Semantic search** using FAISS + OpenAI embeddings
* 📚 **Source metadata** shown: volume, book, narrator, number
* 🧠 Fully functional **Retrieval-Augmented Generation pipeline**
* ⚙️ **Reproducible index-building** pipeline from raw JSON
* 🌐 **Streamlit interface** — ask questions in natural language via browser

---

## 📚 About the Dataset: Sahih al-Bukhari

This project is based on the full content of **Sahih al-Bukhari**, one of the most authentic and respected hadith collections in Sunni Islam. Compiled by the scholar **Imam Muhammad ibn Ismail al-Bukhari** (d. 870 CE), the book contains over **7,000 hadiths**, including repetitions, and covers a wide range of topics relevant to Islamic belief, law, worship, ethics, and daily life.

The collection is organized into **93 thematic books** (*kutub*), such as:

* Book 1: Revelation (*Kitāb Badʾ al-Waḥy*)
* Book 4: Ablution (*Kitāb al-Wuḍūʾ*)
* Book 69: Drinks (*Kitāb al-Ashriba*)
* Book 77: Dress (*Kitāb al-Libās*)
  ...and many others.

### 📥 Data Source

The base dataset was adapted from the excellent open-source repository
👉 [essaji/Complete-Sahih-Bukhari-Json](https://github.com/essaji/Complete-Sahih-Bukhari-Json)

All hadiths were normalized into a flat format, enriched with metadata (volume, book, number, narrator), and made searchable through vector indexing.

---

## 🧪 Example Queries and Real Responses

### ❓ **What breaks the fast during Ramadan?**

**🧠 Answer:**

> The fast during Ramadan is broken by consuming food, drink, or engaging in sexual activity during the daylight hours.

**📌 Source Hadith(s):**

1. **Narrator:** *Umar bin Al-Khattab*
   📖 *"When night falls from this side and the day vanishes from this side and the sun sets, then the fasting person should break his fast."*
   `Vol. 3 | Book 31 | No. 175`

2. **Narrator:** *Anas*
   📖 *"Do not practice Al-Wisal..." — The Prophet replied, "I am not like any of you, for I am given food and drink (by Allah) during the night."*
   `Vol. 3 | Book 31 | No. 182`

3. **Narrator:** *Ibn 'Abbas*
   📖 *"Once the Prophet set out in the month of Ramadan. He observed fasting till he reached a place called Kadid where he broke his fast."*
   `Vol. 4 | Book 52 | No. 202`

4. **Narrator:** *Abu Huraira*
   📖 *"The Fast is for Me... as he leaves his sexual desire, food and drink for My Sake."*
   `Vol. 9 | Book 93 | No. 584`

---

### 📖 What should one say before sleeping?

**Answer:**
Before sleeping, one can say the following supplication:
**"Bismika Rabbi wada'tu Janbi wa bika arfa'uhu, In amsakta nafsi farhamha wa in arsaltaha fahfazha bima tahfazu bihi ibadakas-salihin."**
Additionally:
**"Allhumma bismika ahya wa amut."**

**Source Hadith(s):**

1. *"He should say: 'Bismika Rabbi wada'tu Janbi wa bika arfa'uhu...'"*
   **Vol. 8 | Book 75 | No. 332 | Narrator:** Abu Huraira

2. *"If anyone of you feels drowsy while praying, he should sleep..."*
   **Vol. 1 | Book 4 | No. 212 | Narrator:** Anas

3. *"If anyone of you feels drowsy while praying he should go to bed..."*
   **Vol. 1 | Book 4 | No. 211 | Narrator:** Aisha

4. *"When the Prophet went to bed, he used to say: 'Allhumma bismika ahya wa amut.'..."*
   **Vol. 9 | Book 93 | No. 491 | Narrator:** Juhaifa

---

### 📖 What is the reward of night prayer?

**Answer:**
The reward of establishing prayers on the night of Qadr (Laylat al-Qadr) out of sincere faith and hoping to attain Allah's rewards is that all past sins will be forgiven.

**Source Hadith(s):**

1. *"The reward of a prayer in congregation is twenty five times greater...*"
   **Vol. 1 | Book 11 | No. 621 | Narrator:** Abu Salama bin 'Abdur Rahman

2. *"A prayer performed in congregation is twenty-five times more superior..."*
   **Vol. 6 | Book 60 | No. 241 | Narrator:** Ibn Al-Musaiyab

3. *"Whoever establishes the prayers on the night of Qadr... all his past sins will be forgiven."*
   **Vol. 1 | Book 2 | No. 34 | Narrator:** Abu Huraira

4. *"If the people knew what is the reward of making the call (for the prayer)..."*
   **Vol. 3 | Book 48 | No. 854 | Narrator:** Abu Huraira

---

📌 **All hadiths — including book numbers, hadith numbers, and narrators — match the structure of [sahih-bukhari.com](http://www.sahih-bukhari.com) and can be cross-verified there.**

---

## ▶️ Quick Start

```bash
git clone https://github.com/Quchluk/al-Bukhari-Hadith-RAG.git
cd al-Bukhari-Hadith-RAG
pip install -r requirements.txt

Configure your OpenAI API key:

cp .env.example .env
# then open .env and paste your key

Run the app:

streamlit run app.py

Open http://localhost:8501 in your browser.
```

---

🧱 Repository Structure

```
al-bukhari-rag/
├── app.py                   # Streamlit app
├── build_index.py           # Builds FAISS index from normalized JSONL
├── faiss_index/             # Optional prebuilt FAISS index (index.faiss, index.pkl)
├── Data/
│   ├── sahih_bukhari.json               # Raw data (optional)
│   └── sahih_bukhari_normalized.jsonl  # Normalized JSONL (one hadith per line)
├── preprocessing/
│   ├── normalize_hadiths.py # Script for normalizing the hadiths
│   └── README.md            # Explanation of preprocessing
├── requirements.txt
├── .env.example             # Template for environment config
├── .gitignore
├── LICENSE
└── README.md                # This file
```

---

🧠 Using the Prebuilt Index

If using the bundled FAISS index:

FAISS.load\_local(path, embeddings, allow\_dangerous\_deserialization=True)

Or you can build it yourself (see below).

---

🛠 Rebuilding the Index

```bash
python preprocessing/normalize_hadiths.py \
  --input Data/sahih_bukhari_raw.json \
  --output Data/sahih_bukhari_normalized.jsonl

python build_index.py
```

To swap out OpenAI for HuggingFace or other models, modify the embedding class in build\_index.py.

---

💡 Applications

* 🧾 Islamic Knowledge QA systems
* 🌍 Multilingual low-resource RAG pipelines
* 🏛 Digital Humanities research
* 📚 Educational bots based on classical texts
* 🧪 Experimentation with domain-specific vector search

---

📚 Data Source

Hadith data adapted from:
essaji/Complete-Sahih-Bukhari-Json

All other code, normalization, interface, and indexing steps are original.

---

🛡 License

This project is licensed under the MIT License.
See the LICENSE file for full terms.

---

👤 Author

Made by Anton Smirnov
Feel free to fork, cite, or build upon this project.
