from flask_testing import TestCase
from flask import current_app, url_for

from main import app


class MainTest(TestCase):

    def create_app(self) -> object:
        app.config["TESTING"] = True
        app.config["WTF_CSRF_ENABLED"] = False
        return app
    
    def test_app_exists(self) -> None:
        self.assertIsNotNone(current_app)

    def test_app_in_test_mode(self) -> None:
        self.assertTrue(current_app.config["TESTING"])

    def test_index_redirects(self) -> None:
        response = self.client.get(url_for("index"))
        # self.assertRedirects(response, )

    def test_hello_get(self) -> None:
        response = self.client.get(url_for("hello"))
        self.assert200(response)

    def test_hello_post(self) -> None:
        fake_form = {
            "username": "fake_username",
            "password": "fake_password"
        }
        response = self.client.post(url_for("hello"), data=fake_form)
        # self.assertRedirects(response, url_for("index"))
