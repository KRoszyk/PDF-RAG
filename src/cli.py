import click
import yaml

from langchain_huggingface import HuggingFaceEmbeddings
from src.pdf_to_text.extraction import get_sentences_from_pdf
from src.llm.model import LLM
from vector_db.initialize import create_vector_db


@click.command()
@click.option('--config', '-c', default='../config.yaml', help='Path to the configuration file')
def run_pipeline(config) -> None:
    with open(config, 'r') as file:
        config_data = yaml.safe_load(file)

        pdf_path = config_data.get('pdf_path')  # load path to pdf
        embedding_model_name = config_data.get('embedding_model_name')  # load name of embedding model
        llm_model_name = config_data.get('llm_model_name')  # load name of llm model
        vector_db_path = config_data.get('vector_db_path')  # load path to save vector db
        template = config_data.get('template')  # load template

        embedding_model = HuggingFaceEmbeddings(model_name=embedding_model_name)  # load embedding model

        sentences = get_sentences_from_pdf(pdf_path)  # function return sentences from pdf
        create_vector_db(sentences, embedding_model, vector_db_path)  # function create vector db

        llm_object = LLM(llm_model_name, template, embedding_model)  # create object
        llm_object.load_vector_db(vector_db_path)  # load vector db (We need to load the vector database every time a new PDF file is uploaded!)
        llm_object.question = "Co wyższe wykształcenie mówi o drugim progu?"  # change question
        answer = llm_object.generate_answer()  # bielik generate answer


if __name__ == "__main__":
    run_pipeline()
