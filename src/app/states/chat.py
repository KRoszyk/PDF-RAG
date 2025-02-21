from pydantic import BaseModel


class AssistanceMessage(BaseModel):
    name: str = "assistant"
    content: str


class UserMessage(BaseModel):
    name: str = "user"
    content: str


class ChatState(BaseModel):
    messages: list[AssistanceMessage | UserMessage] = []
    container_height: int = 5000  # Size of the message container. It should be big because then it stays responsive.
    input_text_info: str = "Enter your message:"
    disabled: bool = True
    trigger_new_prompt: bool = False
    prompt: str = ""
    key: str = "chat"

    def clear_chat(self) -> None:
        self.messages.clear()
