import yaml
import click
from interface.app import create_gui


def load_config(config_path):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config


@click.command()
@click.option('--config-path', default='config.yaml', help='Path to the .yaml file')
def run_pipeline(config_path) -> None:
    config = load_config(config_path)
    path_file = config['paths']['path_pdf']
    path_modified_file = config['paths']['path_modified_pdf']
    message_container_height = config['message_container_height']
    layout_division = config['layout_division']

    create_gui(path_file, path_modified_file, message_container_height, layout_division)


if __name__ == "__main__":
    run_pipeline()
