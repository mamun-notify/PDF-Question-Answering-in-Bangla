import re

def sentence_chunker(input_path, output_path, chunk_size=3):
    with open(input_path, "r", encoding="utf-8") as f:
        text = f.read()

    sentences = re.split(r'(?<=[।?!])\s+', text)
    chunks = [" ".join(sentences[i:i+chunk_size]).strip()
              for i in range(0, len(sentences), chunk_size)]

    with open(output_path, "w", encoding="utf-8") as out:
        for chunk in chunks:
            out.write(chunk + "\n---\n")
    print(f"✅ Chunks saved to: {output_path}")
    return chunks
