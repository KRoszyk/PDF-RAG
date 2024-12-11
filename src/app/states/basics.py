from pydantic import BaseModel


class ButtonState(BaseModel):
    name: str = ""


class TitleState(BaseModel):
    text: str = ""
    key: str = ""
