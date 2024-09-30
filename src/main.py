import click
import yaml
from langchain_huggingface import HuggingFaceEmbeddings
from src.pdf_to_text.extraction import get_sentences_from_pdf
from vector_db.vector_db import create_vector_db


@click.command()
@click.option('--config', '-c', default='../config.yaml', help='Path to the configuration file')
def run_pipeline(config) -> None:
    with open(config, 'r') as file:
        config_data = yaml.safe_load(file)

        pdf_path = config_data.get('pdf_path')  # load path to pdf
        embedding_model_name = config_data.get('embedding_model_name')  # load name of embedding model
        vector_db_path = config_data.get('vector_db_path')   # load path to save vector db

        embedding_model = HuggingFaceEmbeddings(model_name=embedding_model_name)  # load embedding model
        sentences = get_sentences_from_pdf(pdf_path)
        create_vector_db(sentences, embedding_model, vector_db_path)


if __name__ == "__main__":
    run_pipeline()
