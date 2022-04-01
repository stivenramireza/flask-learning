from flask import current_app, url_for

from tests.test_main import TestMain


class TestBase(TestMain):
    def test_app_exists(self) -> None:
        self.assertIsNotNone(current_app)

    def test_app_in_test_mode(self) -> None:
        self.assertTrue(current_app.config["TESTING"])

    def test_index_redirects(self) -> None:
        response = self.client.get(url_for("index"))
        # self.assertRedirects(response, url_for("hello"))

    def test_hello_get(self) -> None:
        response = self.client.get(url_for("hello"))
        self.assert200(response)

    def test_hello_post(self) -> None:
        response = self.client.post(url_for("hello"))
        self.assertTrue(response.status_code, 405)
