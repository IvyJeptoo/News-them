from flask import Flask
from .config import DevConfig


app = Flask(__name__)
app.config.from_objects(DevConfig)

from app import views
