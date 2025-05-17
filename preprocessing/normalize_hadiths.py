import json
import re

def clean_text(text):
    text = text.replace('\r', ' ').replace('\n', ' ') 
    text = text.replace('\\"', '"').replace("“", '"').replace("”", '"')
    text = re.sub(r'\s+', ' ', text) 
    return text.strip()

def extract_number(info_field):
    match = re.search(r'Number\s+(\d+)', info_field)
    return match.group(1) if match else "unknown"

def normalize_hadiths(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    normalized = []
    for vol in data:
        volume = vol.get("name", "unknown volume")
        for book in vol.get("books", []):
            book_name = book.get("name", "unknown book")
            for h in book.get("hadiths", []):
                hadith_number = extract_number(h.get("info", ""))
                narrator = clean_text(h.get("by", ""))
                text = clean_text(h.get("text", ""))
                source_id = f"{volume} | {book_name} | {hadith_number}"

                normalized.append({
                    "text": text,
                    "metadata": {
                        "volume": volume,
                        "book": book_name,
                        "number": hadith_number,
                        "narrator": narrator,
                        "source_id": source_id
                    }
                })

    with open(output_path, 'w', encoding='utf-8') as f:
        for entry in normalized:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    print(f"✓ Normalized {len(normalized)} hadiths saved to {output_path}")

normalize_hadiths("/Users/Tosha/Desktop/al-Buhari RAG application/Data/sahih_bukhari.json", "/Users/Tosha/Desktop/al-Buhari RAG application/Data/sahih_bukhari_normalized.json")
