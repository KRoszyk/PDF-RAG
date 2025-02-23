from typing import Any

from attrs import define, Factory
import spacy
from spacy_layout import spaCyLayout
import json
from src.rag.config import JsonPath


@define
class TextExtractor:
    file: bytes
    json_config: JsonPath = JsonPath()
    sentences: list[str] = Factory(list)
    spans_metadata: list[dict[str, dict[str, Any]]] = []

    def __attrs_post_init__(self):
        nlp = spacy.blank("en")
        layout = spaCyLayout(nlp)
        doc = layout(self.file)
        self.spans_metadata = []
        self.sentences = []

        for span in doc.spans["layout"]:

            # Filter data
            if len(span.text) < 3:
                continue

            layout_data = span._.layout
            span_info = {
                "text": span.text,
                "page_no": layout_data.page_no,
                "bounding_box": {
                    "x": layout_data.x,
                    "y": layout_data.y,
                    "width": layout_data.width,
                    "height": layout_data.height
                }
            }
            self.spans_metadata.append(span_info)
            self.sentences.append(span.text)

        with open(self.json_config.json_path, 'w', encoding='utf-8') as f:
            json.dump(self.spans_metadata, f, ensure_ascii=False, indent=4)
