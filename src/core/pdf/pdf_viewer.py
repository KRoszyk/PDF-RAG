from attrs import define
from streamlit_pdf_viewer import pdf_viewer

from src.states.gui import GUIState


@define
class PdfViewer:
    state: GUIState

    def __attrs_post_init__(self):
        uploader_state = self.state.left_col.uploader

        if uploader_state.is_file_uploaded is True:
            pdf_viewer(
                input=uploader_state.file,
                key=self.state.right_col.pdf_viewer.key
            )
