# 📄 PDF Question Answering in Bangla

Welcome!  
This project demonstrates how to convert Bangla PDF documents into a searchable knowledge base that supports automatic question answering using OCR, NLP preprocessing, semantic embedding, and local language models.

---

## 🚀 Features

- ✅ Convert scanned or digital PDFs to Bangla text using OCR
- ✅ Clean, normalize, and chunk content intelligently
- ✅ Generate semantic vector embeddings for each chunk
- ✅ Store chunks using FAISS for fast similarity search
- ✅ Ask Bangla questions and receive contextual answers in real-time

---

## 📁 Project Structure

project/  
├── data/ # PNG images (1 per page) exported from PDF  
├── output/ # All generated files (text, chunks, embeddings)  
│ ├── extracted.txt  
│ ├── cleaned.md  
│ ├── normalized.txt  
│ ├── chunks.txt  
│ └── answer.txt  
├── steps/ # Modular steps (OCR, clean, normalize, embed, QA)  
├── main.py # Main pipeline script  
└── requirements.txt



---

## 🛠️ Setup Guide

### 1️⃣ Convert PDF to Images
Export your PDF pages as `.png` images (e.g. using Adobe Acrobat or other tools) and save them inside the `data/` folder.

### 2️⃣ Set up Python Environment
```bash
python -m venv venv
# Activate on Windows
venv\Scripts\activate
# Or on Linux/macOS
source venv/bin/activate
```

### 3️⃣ Install Requirements

`pip install -r requirements.txt`

### 4️⃣ Run the Pipeline

`python main.py`


## 📤 Output

The following files will be generated in the `output/` folder:

-   `extracted.txt` – Raw OCR output
    
-   `cleaned.md` – Cleaned and markdown-formatted content
    
-   `normalized.txt` – Normalized Bangla text
    
-   `chunks.txt` – Text chunks used for retrieval
    
-   `answer.txt` – Final answer generated based on your query

## 💬 Sample Queries

### Bangla

প্রশ্ন: অনুপমের ভাষায় সুপুরুষ কাকে বলা হয়েছে?
উত্তর: কী

প্রশ্ন: কাকে অনুপমের ভাগ্য দেবতা বলে উল্লেখ করা হয়েছে?
উত্তর: অপরিচিতা

প্রশ্ন: বিয়ের সময় কল্যাণীর প্রকৃত বয়স কত ছিল?
উত্তর: ২৮ বছর

প্রশ্ন: বিদ্রোহী কবিতার মূল বার্তা কী?
উত্তর: মীমাংসা

প্রশ্ন: অনুপম চরিত্রের বৈশিষ্ট্য কী?
উত্তর: বৈসাদৃশ্যপূর্ণ

প্রশ্ন: কল্যাণী চরিত্রটি কী উপস্থাপন করে?
উত্তর: হারুন মিয়া

প্রশ্ন: অপরিচিতা গল্পের পটভূমি কী?
উত্তর: জোড়ার্সাকোর ঠাকুর বাড়িতে

প্রশ্ন: পণপ্রথার কুপ্রভাব কীভাবে দেখানো হয়েছে?
উত্তর: ধর্মনিষ্ঠা


### 🧰 Tools & Libraries Used

| Tool / Library       | Purpose / Role                                  |
|----------------------|--------------------------------------------------|
| Python               | Core programming language                       |
| PaddleOCR            | OCR engine with Bengali language support        |
| SentenceTransformers | Generating semantic embeddings from text        |
| FAISS                | Vector similarity search                        |
| Hugging Face         | Pretrained models and transformers              |
| PyMuPDF / PIL        | PDF and image handling                          |
| BanglaBERT           | Bengali language understanding & QA             |


## 🧠 Design & Methodology Q&A

### 🅠 What method or library did you use to extract the text, and why?

I have used **PaddleOCR** with Bangla language support because of its strong multilingual capabilities and good accuracy on printed text.  
📌 Challenge: The PDF was converted to images, and OCR sometimes produced broken words, which were handled via post-cleaning.

----------

### 🅠 What chunking strategy did you use?

I have used a **sentence-based chunking** approach, grouping 2–3 Bangla sentences per chunk.  
✅ Sentence chunking works well for semantic retrieval because:

-   It preserves topic continuity
    
-   Avoids arbitrary cuts
    
-   Helps align with user questions that typically span sentence-level logic
    
----------

### 🅠 What embedding model did you use? Why?

I have used a **multilingual MiniLM-based SentenceTransformer** model:  
`sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`  
✅ It supports Bangla, produces fast dense embeddings, and works well for low-resource languages.

----------

### 🅠 How is the query compared with the document chunks?

I have used **cosine similarity** between the embedding of the user query and each chunk vector stored in **FAISS**.  
✅ FAISS is chosen for speed and scalability, even with thousands of chunks.

----------

### 🅠 How do you ensure meaningful comparisons?

-   Used the same embedding model for both query and chunks
    
-   All text is normalized and preprocessed before vectorization
    
-   Selected **top-k similar chunks** to build the prompt context
    

📉 If the query is vague or missing context, results may be off — better prompts and more contextual chunking can help.

----------

### 🅠 Do the results seem relevant?

Partially — depending on the OCR quality and model capabilities.  
❌ Sometimes the QA model returns incorrect or incomplete answers.  
🚧 Future Improvements:

-   Use larger, instruction-tuned models (e.g. LLaMA-based)
    
-   Fine-tune chunking and QA prompt construction
    
-   Better OCR post-processing to improve text quality