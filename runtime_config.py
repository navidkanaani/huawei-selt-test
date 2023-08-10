import os
from os.path import join, dirname
from dotenv import load_dotenv


dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

class RuntimeConfig:
    USERNAME = os.environ.get("FANAVA_USERNAME")
    PASSWORD = os.environ.get("FANAVA_PASSWORD")
