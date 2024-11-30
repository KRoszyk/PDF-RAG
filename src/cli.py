from src.rag.rag import RAG


def run_pipeline() -> None:
    rag = RAG()
    print(rag.predict("Co składa się na budżet czasu?"))
    print(rag.predict("Co podkreśla Tarkowska??"))


if __name__ == "__main__":
    run_pipeline()
