from flask import Flask

app = Flask(__name__)

# Import views late to avoid circular imports
from app import main
from app import auth
from app import todos
from app import uptime
