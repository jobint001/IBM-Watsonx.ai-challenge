from flask import Flask
from dotenv import load_dotenv
import os
from flask_cors import CORS, cross_origin




def create_app():
    app = Flask(__name__)
    CORS(app, support_credentials=True)
    # Load configuration
    load_dotenv()
    
    app.config['API_KEY'] = os.getenv('API_KEY')
    app.config['PROJECT_ID'] = os.getenv('PROJECT_ID')

    # Register Blueprints
    from app.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
