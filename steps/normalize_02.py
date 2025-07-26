import re

def basic_bangla_normalize(input_path, output_path):
    with open(input_path, "r", encoding="utf-8") as f:
        text = f.read()

    text = re.sub(r'[“”]', '"', text)
    text = re.sub(r"[‘’]", "'", text)
    text = re.sub(r"(\r\n|\r|\n)+", "\n", text)
    text = re.sub(r"[^\u0980-\u09FF \n.,?!;:'\"(){}[\]০-৯]+", " ", text)
    text = re.sub(r"্+", "্", text)
    text = re.sub(r" +", " ", text)

    with open(output_path, "w", encoding="utf-8") as out:
        out.write(text)
    print(f"✅ Normalized text saved to: {output_path}")
