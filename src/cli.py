from src.rag.rag import Rag


def run_pipeline() -> None:
    rag = Rag()
    rag.create_sentences()
    rag.create_vector_db()
    rag.load_vector_db()
    print(rag.predict("Do czego odnosi sie drugi próg?"))
    print(rag.predict("Jaki jest tytul 1 rozdziału?"))


if __name__ == "__main__":
    run_pipeline()
