import spacy
import pdfplumber

nlp = spacy.load("en_core_web_sm")


def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
    text = text.replace("\n", " ").replace("\r", "").strip()
    return text


def split_text_into_sentences(text):
    doc = nlp(text)
    sentences = [sent.text.strip() for sent in doc.sents if len(sent.text.strip()) > 0]
    return sentences


def get_sentences_from_pdf(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    sentences = split_text_into_sentences(text)
    return sentences
