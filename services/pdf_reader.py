import fitz


def extract_pdf_text(pdf_path):
    doc = fitz.open(pdf_path)

    text = ""

    for page in doc:
        text += page.get_text()

    pages = len(doc)

    doc.close()

    return text, pages


def create_summary(text, max_chars=1000):
    text = text.replace("\n", " ").strip()

    if len(text) <= max_chars:
        return text

    return text[:max_chars] + "..."
