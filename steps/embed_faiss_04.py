from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

def embed_chunks(input_path):
    with open(input_path, "r", encoding="utf-8") as f:
        chunks = [c.strip() for c in f.read().split("\n---\n") if c.strip()]

    model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
    embeddings = model.encode(chunks)
    
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))

    print("✅ FAISS index created and populated.")
    return model, index, chunks
