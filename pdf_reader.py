import fitz

def get_pages(path):
    pdf = fitz.open(path)
    return len(pdf)
