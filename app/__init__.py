from flask import Flask

from app.health import health_bp

app = Flask(__name__)
app.register_blueprint(health_bp)

# Import routes
from app import main
