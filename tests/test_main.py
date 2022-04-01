from flask_testing import TestCase

from main import app


class TestMain(TestCase):
    def create_app(self) -> object:
        app.config["TESTING"] = True
        app.config["WTF_CSRF_ENABLED"] = False
        return app
