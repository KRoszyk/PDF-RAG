from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


def create_vector_db(sentences):
    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
    text_embeddings = embedding_model.embed_documents(sentences)
    text_embedding_pairs = list(zip(sentences, text_embeddings))
    vector_db = FAISS.from_embeddings(text_embedding_pairs, embedding_model)
    vector_db.save_local("../vector_db_faiss")
