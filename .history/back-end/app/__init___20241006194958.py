from flask import Flask
from config import Config
from flask_cors import CORS


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # 跨域支持
    CORS(app)

    # 注册 blueprint
    from app.api import bp as api_bp

    app.register_blueprint(api_bp, url_prefix="/api")

    return app
