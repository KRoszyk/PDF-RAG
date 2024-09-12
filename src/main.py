import streamlit as st
from src.gui import app
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

    if 'file_name' not in st.session_state:
        st.session_state['file_name'] = 'No file selected'
    if 'file_loaded' not in st.session_state:
        st.session_state['file_loaded'] = False
    if 'uploaded_file' not in st.session_state:
        st.session_state['uploaded_file'] = None
    if 'generated_text' not in st.session_state:
        st.session_state['generated_text'] = ''

    app.create_gui(path)


if __name__ == "__main__":
    main()