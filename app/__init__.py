from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)

    #imports hello_world_bp and has blueprint register it as a route
    from .routes import hello_world_bp
    app.register_blueprint(hello_world_bp)

    return app
