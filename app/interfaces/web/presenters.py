from flask import Flask

def create_app():
    app = Flask(__name__)

    # Load the configuration from config.py
    app.config.from_pyfile('config.py')

    # Register the web blueprint
    from app.interfaces.web import bp as web_bp
    app.register_blueprint(web_bp)

    return app
