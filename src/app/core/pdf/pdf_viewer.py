import json
from attrs import define
from streamlit_pdf_viewer import pdf_viewer
import fitz
from src.app.states.gui import GUIState
import io


@define
class PdfViewer:
    state: GUIState
    actual_scroll_position: int

    def __attrs_post_init__(self):
        uploader_state = self.state.left_col.uploader

        pdf_file = uploader_state.file

        if uploader_state.is_file_uploaded is True:
            pdf_viewer(
                input=self.mark_text(pdf_file),
                annotations=self.state.right_col.pdf_viewer.annotations,
                scroll_to_annotation=self.actual_scroll_position,
                key=self.state.right_col.pdf_viewer.key
            )

    def mark_text(self, pdf_file: bytes):
        if len(self.state.right_col.pdf_viewer.phrases_to_highlight) > 0:
            self.state.right_col.pdf_viewer.annotations = []
            with open(self.state.right_col.pdf_viewer.json_path, 'r', encoding='utf-8') as f:
                spans = json.load(f)

            pdf_document = fitz.open("pdf", pdf_file)

            for span in spans:
                page_number = span["page_no"] - 1
                x = span["bounding_box"]["x"]
                y = span["bounding_box"]["y"]
                width = span["bounding_box"]["width"]
                height = span["bounding_box"]["height"]
                text = span.get("text", "")

                for phrase in self.state.right_col.pdf_viewer.phrases_to_highlight:
                    if phrase == text:
                        page = pdf_document.load_page(page_number)
                        rect = fitz.Rect(x, y, x + width, y + height)
                        page.draw_rect(rect, color=(1, 0, 0), width=2, fill=None)
                        self.state.right_col.pdf_viewer.annotations.append({
                            "page": span["page_no"],
                            "x": x,
                            "y": y,
                            "width": width,
                            "height": height,
                        })

            output_pdf_bytes = io.BytesIO()
            pdf_document.save(output_pdf_bytes)
            output_pdf_bytes.seek(0)
            self.state.right_col.pdf_viewer.update_key()
            self.state.right_col.pdf_viewer.phrases_to_highlight = []
            self.state.right_col.content_counter.scroll_count = len(self.state.right_col.pdf_viewer.annotations)
            self.state.right_col.content_counter.actual_scroll_position = 1
            return output_pdf_bytes.read()
        else:
            return pdf_file
