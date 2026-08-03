import fitz
import re


class PDFManager:

    def __init__(self, path):

        self.path = path

    def extract(self):

        doc = fitz.open(self.path)

        pages = len(doc)

        text = ""

        for page in doc:

            try:
                text += page.get_text()
            except Exception:
                pass

        doc.close()

        text = self.clean(text)

        summary = self.summary(text)

        title = self.title(text)

        author = self.author(text)

        return {
            "title": title,
            "author": author,
            "pages": pages,
            "summary": summary,
            "text": text,
        }

    def clean(self, text):

        text = text.replace("\x00", "")

        text = re.sub(r"\n+", "\n", text)

        text = re.sub(r"\s+", " ", text)

        return text.strip()

    def summary(self, text):

        if len(text) < 2000:
            return text

        return text[:2000]

    def title(self, text):

        lines = text.split("\n")

        for line in lines[:15]:

            line = line.strip()

            if len(line) > 6:
                return line

        return "بدون عنوان"

    def author(self, text):

        keywords = [
            "إعداد",
            "المؤلف",
            "بقلم",
            "تأليف"
        ]

        for key in keywords:

            i = text.find(key)

            if i != -1:

                return text[i:i+80]

        return "غير معروف"
