from flask import url_for

from tests.test_main import TestMain


class TestAuth(TestMain):
    def test_auth_blueprint_exists(self) -> None:
        self.assertIn("auth", self.app.blueprints)

    def test_auth_login_get(self) -> None:
        response = self.client.get(url_for("auth.login"))
        self.assert200(response)

    def test_auth_login_get(self) -> None:
        self.client.get(url_for("auth.login"))
        self.assertTemplateUsed("login.html")

    def test_auth_login_post(self) -> None:
        fake_form = {"username": "fake_username", "password": "fake_password"}

        response = self.client.post(url_for("auth.login"), data=fake_form)
        # self.assertRedirects(response, url_for("index"))
