from src.rag.interface import RAGInterface


def run_pipeline() -> None:
    rag = RAGInterface()

    questions = [
        "Do czego odnosi sie drugi próg?",
        "Jaki jest tytul 1 rozdziału?",
        "Jaka jest procentowa stawka VAT w Polsce?"
    ]

    for question in questions:
        rag_answer = rag.invoke(question)
        print(rag_answer)


if __name__ == "__main__":
    run_pipeline()
