import json
from attrs import define
from streamlit_pdf_viewer import pdf_viewer
import streamlit as st
import fitz
from src.app.states.gui import GUIState
import io


@define
class PdfViewer:
    state: GUIState
    page_number: int | None = None

    def __attrs_post_init__(self):
        uploader_state = self.state.left_col.uploader

        pdf_file = uploader_state.file

        if uploader_state.is_file_uploaded is True:
            modified_pdf = self.mark_text(pdf_file)
            pdf_viewer(
                input=modified_pdf,
                scroll_to_page=self.page_number,
                key=self.state.right_col.pdf_viewer.key
            )

    def mark_text(self, pdf_file: bytes) -> bytes:
        pages_with_highlighted_text = []

        if len(self.state.right_col.pdf_viewer.phrases_to_highlight) > 0:
            with open(self.state.right_col.pdf_viewer.json_path, 'r', encoding='utf-8') as f:
                spans = json.load(f)

            pdf_document = fitz.open("pdf", pdf_file)

            for span in spans:
                page_number = span["page_no"] - 1
                x, y, width, height = span["bounding_box"].values()
                text = span.get("text", "")

                if any(phrase.lower() in text.lower() for phrase in self.state.right_col.pdf_viewer.phrases_to_highlight):
                    page = pdf_document.load_page(page_number)
                    rect = fitz.Rect(x, y, x + width, y + height)
                    page.draw_rect(rect, color=(1, 0, 0), width=2)
                    pages_with_highlighted_text.append(page_number+1)

            pages_with_highlighted_text=list(set(pages_with_highlighted_text))
            output_pdf_bytes = io.BytesIO()
            pdf_document.save(output_pdf_bytes)
            output_pdf_bytes.seek(0)
            self.state.right_col.found_pages.change_pages(pages=pages_with_highlighted_text)
            self.state.right_col.pdf_viewer.update_key()
            self.state.right_col.pdf_viewer.phrases_to_highlight = []
            return output_pdf_bytes.read()
        else:
            return pdf_file

