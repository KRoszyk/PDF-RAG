from pydantic import BaseModel


class PdfPath(BaseModel):
    pdf_path: str = "data/pdf/styl.pdf"


class VectorDBConfig(BaseModel):
    vector_db_path: str = "data/db_faiss"
    top_k: int = 5


class EmbeddingModelConfig(BaseModel):
    embeddings_model_name: str = "sdadas/mmlw-roberta-large"


class LLMConfig(BaseModel):
    llm_model_name: str = "mwiewior/bielik"
    prompt: str = """
    Jesteś asystentem AI z dostępem do bazy wiedzy stworzonej z paragrafów dokumentu. 
    Na podstawie poniższego kontekstu:
    <CONTEXT>{context}</CONTEXT>
    
    Udziel zwięzłej odpowiedzi na poniższe pytanie w maksymalnie dwóch zdaniach, 
    opierając się TYLKO na informacjach podanych w kontekście: 
    {input}
    
    Unikaj dodatkowych tagów takich jak "Odpowiedź:" w swojej odpowiedzi.
    Jeśli nie możesz odpowiedzieć na pytanie, korzystając z podanego kontekstu, wyjaśnij, że nie masz wystarczających 
    informacji, aby udzielić dokładnej odpowiedzi.
    """
