import click
import yaml

from src.pdf_to_text.extraction import get_sentences_from_pdf
from src.llm.model import LLM
from src.llm.embedding_model import  EMBEDDING_MODEL
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

        sentences = get_sentences_from_pdf(pdf_path)  # function return sentences from pdf
        embedding_model = EMBEDDING_MODEL(embedding_model_name)  # create object
        create_vector_db(sentences, embedding_model, vector_db_path)  # function create vector db

        llm_model = LLM(llm_model_name, template)  # create object
        llm_model.load_vector_db(vector_db_path, embedding_model)  # load vector db (We need to load the vector database every time a new PDF file is uploaded!)
        llm_model.predict("Co wyższe wykształcenie mówi o drugim progu?", embedding_model)  # model generate answer


if __name__ == "__main__":
    run_pipeline()
