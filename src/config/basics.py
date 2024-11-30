from pydantic import BaseModel


class DataPaths(BaseModel):
    pdf_path: str = "..\data\pdf\styl.pdf"
    vector_db_path: str = "..\data\db_faiss"


class ModelsNames(BaseModel):
    embedding_model_name: str = "sdadas/mmlw-roberta-large"
    llm_model_name: str = "mwiewior/bielik"


class Template(BaseModel):
    template: str = """Użyj poniższych informacji, aby odpowiedzieć na pytanie na końcu. 
    Jeśli nie znasz odpowiedzi, po prostu powiedz, że nie wiesz, i nie próbuj wymyślać 
    odpowiedzi. Użyj maksymalnie trzech zdań i postaraj się, aby odpowiedź była jak najkrótsza. 
    Zawsze dodaj "dziękuję za pytanie!" na końcu swojej odpowiedzi. {context} Pytanie: {question} Pomocna odpowiedź: """
