from flask import Flask
from dotenv import load_dotenv
import os

def create_app():
    app = Flask(__name__)
    
    # Load configuration
    load_dotenv()
    
    app.config['API_KEY'] = os.getenv('API_KEY')

    # Register Blueprints
    from app.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
