from pypdf import PdfReader


def extract_text_from_pdf(path) -> str:
    reader = PdfReader(path)

    all_text = ""

    for page in reader.pages:
        all_text += page.extract_text() + "\n"

    return all_text