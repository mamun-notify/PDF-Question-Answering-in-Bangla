# import os
# from openai import OpenAI

# client = OpenAI()  # This automatically picks OPENAI_API_KEY from env

# def retrieve_top_k(query, model, index, chunks, k=5):
#     query_vec = model.encode([query])
#     distances, indices = index.search(query_vec, k)
#     return [chunks[i] for i in indices[0]]

# def generate_answer(query, context_chunks):
#     context = "\n".join(context_chunks)
#     prompt = f"""Answer the following question based on the context below.

# Context:
# {context}

# Question: {query}
# Answer:"""

#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo",  # or "gpt-4"
#         messages=[{"role": "user", "content": prompt}],
#         temperature=0.2
#     )
#     return response.choices[0].message.content

# steps/retrieve_generate_05.py
import torch
from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline

# Load model and tokenizer once
MODEL_NAME = "sagorsarker/mbert-bengali-tydiqa-qa"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForQuestionAnswering.from_pretrained(MODEL_NAME)

qa_pipeline = pipeline(
    "question-answering",
    model=model,
    tokenizer=tokenizer,
    device=0 if torch.cuda.is_available() else -1
)

def retrieve_top_k(query, model_emb, index, chunks, k=5):
    query_vec = model_emb.encode([query])
    distances, indices = index.search(query_vec, k)
    return [chunks[i] for i in indices[0]]

def generate_answer(query, context_chunks):
    context = " ".join(context_chunks)
    result = qa_pipeline(question=query, context=context)
    return result.get("answer", "উত্তর পাওয়া যায়নি।")
