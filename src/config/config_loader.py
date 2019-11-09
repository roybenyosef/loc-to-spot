import yaml


def read_config():
    file_stream = open("config/config.yaml", "r")
    return yaml.safe_load(file_stream)
