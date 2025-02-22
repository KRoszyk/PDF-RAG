from pydantic import BaseModel


class ButtonState(BaseModel):
    name: str = ""


class TitleState(BaseModel):
    text: str = ""
    key: str = ""


class ScrollCounter(BaseModel):
    scroll_count: int = 0
    actual_scroll_position: int = 0
