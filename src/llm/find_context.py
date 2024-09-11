from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


def similarity(question):
    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
    vector_db = FAISS.load_local("../vector_db_faiss", embedding_model, allow_dangerous_deserialization=True)
    q_embedding = embedding_model.embed_documents([question])[0]
    relevant_doc = vector_db.similarity_search_by_vector(q_embedding, k=1)
    return relevant_doc[0].page_content