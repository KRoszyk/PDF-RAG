from src.module_rag.rag.rag import Rag


def run_pipeline() -> None:
    rag = Rag()
    print(rag.predict("Do czego odnosi sie drugi próg?"))
    print(rag.predict("Jaki jest tytul 1 rozdziału?"))


if __name__ == "__main__":
    run_pipeline()
