import sys
from dotenv import  get_key
from pathlib import Path


def get_root_dir():
    if getattr(sys, "frozen", False):
        root_dir = Path(sys._MEIPASS)   # for PyInstaller when frozen
    else:
        root_dir = Path(__file__).parent.parent   # for development
    return root_dir

def connect_string():
    root_dir = get_root_dir()
    env_path = root_dir / '.env'
    DB_HOST = get_key(env_path, 'DB_HOST')
    DB_PORT = get_key(env_path, 'DB_PORT')
    DB_DATABASE = get_key(env_path, 'DB_DATABASE')
    DB_USER = get_key(env_path, 'DB_USER')
    DB_PASSWORD = get_key(env_path, 'DB_PASSWORD')

    connection_string = (
        f"postgresql://{DB_USER}:{DB_PASSWORD}@"
        f"{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
    )
    return connection_string

