from flask import Flask, jsonify
from tracking.config import Config
from tracking.controller.visit_controller import visit_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(visit_bp, url_prefix='/api/visits')

    @app.route('/')
    def index():
        return jsonify({"message": "Welcome to the tracking service!"})

    return app


app = create_app()

if __name__ == "__main__":
    app.run()