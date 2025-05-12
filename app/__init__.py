from flask import Flask
from app.views.tarot_view import tarot_bp
from app.views.main_view import main_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(main_bp)
    app.register_blueprint(tarot_bp)
    return app
