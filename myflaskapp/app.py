
from html import escape
from importlib.metadata import version

from flask import Flask, jsonify, render_template, request
from config import config_by_name


def create_app(config_name: str = "default") -> Flask:
    # Створення додатка через Application Factory
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    if config_name == "production" and not app.config["SECRET_KEY"]:
        raise RuntimeError("Потрібно встановити FLASK_SECRET_KEY")

    register_routes(app)
    return app


def register_routes(app: Flask) -> None:
    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/about")
    def about():
        return (
            "<h1>Про Flask-проєкт</h1>"
            "<p>Дисципліна: Програмування</p>"
            "<p>Практична робота №5</p>"
        )

    @app.route("/api/info")
    def api_info():
        # Формування JSON-відповіді
        routes = sorted(rule.rule for rule in app.url_map.iter_rules())

        return jsonify(
            framework="Flask",
            version=version("flask"),
            debug=app.debug,
            routes=routes
        )

    @app.route("/greet")
    @app.route("/greet/<name>")
    def greet(name=None):
        # Отримання імені з URL або GET-запиту
        visitor = name or request.args.get("name", "Гість")
        return f"<h1>Привіт, {escape(visitor)}!</h1>"


if __name__ == "__main__":
    application = create_app("development")
    application.run(port=5000)
