import re

def clean_bangla_markdown(input_path, output_path):
    with open(input_path, "r", encoding="utf-8") as f:
        text = f.read()

    text = re.sub(r'^#+\s+', '', text, flags=re.MULTILINE)
    text = re.sub(r'^\*\s+', '', text, flags=re.MULTILINE)
    text = re.sub(r'!\[.*?\]\(.*?\)', '', text)
    text = re.sub(r'\[.*?\]\(.*?\)', '', text)
    text = re.sub(r'\*\*|__|\*|_', '', text)
    text = re.sub(r'\n{2,}', '\n', text)
    text = re.sub(r'[ \t]+', ' ', text)
    text = re.sub(r'^\s*$', '', text, flags=re.MULTILINE)
    text = re.sub(r'[“”]', '"', text)
    text = re.sub(r"[‘’]", "'", text)
    text = re.sub(r"(\d+)\s+পৃষ্ঠা", '', text)

    with open(output_path, "w", encoding="utf-8") as out:
        out.write(text)
    print(f"✅ Cleaned markdown saved to: {output_path}")
