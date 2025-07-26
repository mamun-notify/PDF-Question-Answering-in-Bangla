from dotenv import load_dotenv
load_dotenv()

from steps import (
    ocr_extract_00,
    clean_md_01,
    normalize_02,
    chunker_03,
    embed_faiss_04,
    retrieve_generate_05
)

# Paths
IMAGE_FOLDER = "data"  # PNG images
EXTRACTED = "output/extracted.txt"
CLEANED = "output/cleaned.md"
NORMALIZED = "output/normalized.txt"
CHUNKS = "output/chunks.txt"

# Step 0: OCR Extraction
ocr_extract_00.extract_text_from_images(IMAGE_FOLDER, EXTRACTED)

# Step 1: Clean markdown (OCR output may not be markdown — you may skip if not needed)
clean_md_01.clean_bangla_markdown(EXTRACTED, CLEANED)

# Step 2: Normalize Bangla
normalize_02.basic_bangla_normalize(CLEANED, NORMALIZED)

# Step 3: Sentence Chunking
chunks = chunker_03.sentence_chunker(NORMALIZED, CHUNKS)

# Step 4: Embedding & FAISS
model, index, loaded_chunks = embed_faiss_04.embed_chunks(CHUNKS)

# Step 5: Ask multiple questions
queries = [
    "অনুপমের ভাষায় সুপুরুষ কাকে বলা হয়েছে?",
    "কাকে অনুপমের ভাগ্য দেবতা বলে উল্লেখ করা হয়েছে?",
    "বিয়ের সময় কল্যাণীর প্রকৃত বয়স কত ছিল?",
    "বিদ্রোহী কবিতার মূল বার্তা কী?",
    "অনুপম চরিত্রের বৈশিষ্ট্য কী?",
    "কল্যাণী চরিত্রটি কী উপস্থাপন করে?",
    "অপরিচিতা গল্পের পটভূমি কী?",
    "পণপ্রথার কুপ্রভাব কীভাবে দেখানো হয়েছে?"
]

OUTPUT_ANSWER = "output/answer.txt"

with open(OUTPUT_ANSWER, "w", encoding="utf-8") as f:
    for query in queries:
        top_chunks = retrieve_generate_05.retrieve_top_k(query, model, index, loaded_chunks)
        answer = retrieve_generate_05.generate_answer(query, top_chunks)
        
        # Print to console
        print(f"\nপ্রশ্ন: {query}")
        print(f"উত্তর: {answer}")
        
        # Write to file
        f.write(f"প্রশ্ন: {query}\n")
        f.write(f"উত্তর: {answer}\n\n")

print(f"\nAll answers saved to: {OUTPUT_ANSWER}")


