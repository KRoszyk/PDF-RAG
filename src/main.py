import click
import yaml
from src.pdf_to_text.extraction import get_sentences_from_pdf


@click.command()
@click.option('--config', '-c', default='../config.yaml', help='Path to the configuration file')
def run_pipeline(config) -> None:
    with open(config, 'r') as file:
        config_data = yaml.safe_load(file)

        pdf_path = config_data.get('pdf_path')  # load path to pdf
        sentences = get_sentences_from_pdf(pdf_path)


if __name__ == "__main__":
    run_pipeline()
