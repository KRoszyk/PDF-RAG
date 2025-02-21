from pydantic import BaseModel


class ButtonState(BaseModel):
    name: str = ""


class TitleState(BaseModel):
    text: str = ""
    key: str = ""


class FoundPages(BaseModel):
    pages: list[int] = []
    actual_page: int = 1

    def change_pages(self, pages: list[int]):
        self.pages = pages
