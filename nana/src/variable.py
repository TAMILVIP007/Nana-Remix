from configparser import ConfigParser
from os import environ

config = ConfigParser()
config.read('config.ini')


def get_var(name, default=None):
    if ENV := bool(environ.get('ENV', False)):
        return environ.get(name, default)

    try:
        return config.get('nana', name)
    except AttributeError:
        return None
