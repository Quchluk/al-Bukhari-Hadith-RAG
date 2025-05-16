# 🕌 al-Bukhari Hadith RAG

A Retrieval-Augmented Generation (RAG) application that answers natural-language questions based on **Sahih al-Bukhari**.  
Built with **LangChain**, **OpenAI embeddings**, **FAISS vector search**, and **Streamlit**.

> ⚡️ Ideal for multilingual and domain-specific retrieval tasks in Digital Humanities and Islamic NLP.

<p align="center">
  <img src="assets/demo.png" alt="Streamlit demo screenshot" width="80%">
</p>

---

## 🚀 Features

- ✅ **7,000+ normalized hadiths** from Sahih al-Bukhari  
- 🔎 **Semantic search** using FAISS + OpenAI embeddings  
- 📚 **Source metadata** shown: volume, book, narrator, number  
- 🧠 Fully functional **Retrieval-Augmented Generation pipeline**  
- ⚙️ **Reproducible index-building** pipeline from raw JSON  
- 🌐 **Streamlit interface** — ask questions in natural language via browser  

---

## 🧪 Example Queries and Real Responses

### 📖 What breaks the fast during Ramadan?

**Answer:**  
The fast during Ramadan is broken by consuming food, drink, or engaging in sexual activity during the daylight hours.

**Source Hadith(s):**

1. *"When night falls from this side and the day vanishes from this side and the sun sets, then the fasting person should break his fast."*  
   **Vol. 3 | Book 31 | No. 175 | Narrator:** Umar bin Al-Khattab

2. *"Do not practice Al-Wisal..." — The Prophet replied, "I am not like any of you, for I am given food and drink (by Allah) during the night."*  
   **Vol. 3 | Book 31 | No. 182 | Narrator:** Anas

3. *"Once the Prophet set out in the month of Ramadan. He observed fasting till he reached a place called Kadid where he broke his fast."*  
   **Vol. 4 | Book 52 | No. 202 | Narrator:** Ibn 'Abbas

4. *"The Fast is for Me... as he leaves his sexual desire, food and drink for My Sake."*  
   **Vol. 9 | Book 93 | No. 584 | Narrator:** Abu Huraira

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

⸻

🧱 Repository Structure

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


⸻

🧠 Using the Prebuilt Index

If using the bundled FAISS index:

FAISS.load_local(path, embeddings, allow_dangerous_deserialization=True)

Or you can build it yourself (see below).

⸻

🛠 Rebuilding the Index

python preprocessing/normalize_hadiths.py \
  --input Data/sahih_bukhari_raw.json \
  --output Data/sahih_bukhari_normalized.jsonl

python build_index.py

To swap out OpenAI for HuggingFace or other models, modify the embedding class in build_index.py.

⸻

💡 Applications
	•	🧾 Islamic Knowledge QA systems
	•	🌍 Multilingual low-resource RAG pipelines
	•	🏛 Digital Humanities research
	•	📚 Educational bots based on classical texts
	•	🧪 Experimentation with domain-specific vector search

⸻

📚 Data Source

Hadith data adapted from:
essaji/Complete-Sahih-Bukhari-Json

All other code, normalization, interface, and indexing steps are original.

⸻

🛡 License

This project is licensed under the MIT License.
See the LICENSE file for full terms.

⸻

👤 Author

Made by Anton Smirnov
Feel free to fork, cite, or build upon this project.
