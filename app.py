from flask import Flask
from routes.post import post_pages
from routes.dashboard import dashboard_pages

def create_app():
    app = Flask(__name__)
    app.register_blueprint(post_pages)
    app.register_blueprint(dashboard_pages)

    return app