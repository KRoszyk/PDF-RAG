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
    global created_object  # użycie zmiennej globalnej

    config = load_config(config_path)
    path_file = config['paths']['path_pdf']
    path_modified_file = config['paths']['path_modified_pdf']

    app.create_gui(path_file, path_modified_file)

if __name__ == "__main__":
    main()
