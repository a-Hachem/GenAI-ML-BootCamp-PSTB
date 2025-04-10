from PyPDF2 import PdfReader

def extract_text_from_pdfs(pdf_files):
    all_text = ""
    for file in pdf_files:
        reader = PdfReader(file)
        for page in reader.pages:
            text = page.extract_text()
            if text:
                all_text += text
    return all_text
