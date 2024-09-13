from gui import app
import yaml
import click


def load_config(config_path):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config


@click.command()
@click.option('--config-path', default='config.yaml', help='Path to the .yaml file')
def main(config_path) -> None:
    config = load_config(config_path)
    path = config['paths']['path_pdf']

    app.create_gui(path)


if __name__ == "__main__":
    main()
