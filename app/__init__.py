from flask import Flask
from time import time

app = Flask(__name__)

# Store the start time of the application
start_time = time()

from app import main
