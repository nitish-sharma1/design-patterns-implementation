from  flask import Flask
from .routes import register_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    # Register Blueprints (for modularity)
    register_routes(app)

    return app
