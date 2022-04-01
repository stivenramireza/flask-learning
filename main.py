import unittest

from flask import (
    request,
    make_response,
    redirect,
    render_template,
    session,
    url_for,
    flash,
)
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

from src.app import create_app

app = create_app()

todos = ["Buy coffee", "Send a sell solicitude", "Deliver video of the product"]


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Send")


@app.route("/")
def index() -> object:
    user_ip = request.remote_addr
    response = make_response(redirect("/hello"))
    session["user_ip"] = user_ip
    return response


@app.route("/hello", methods=["GET", "POST"])
def hello() -> object:
    user_ip = session.get("user_ip")
    login_form = LoginForm()
    username = session.get("username")

    context = {
        "user_ip": user_ip,
        "todos": todos,
        "login_form": login_form,
        "username": username,
    }

    if login_form.validate_on_submit():
        username = login_form.username.data
        session["username"] = username

        flash("Username registered successfully")

        return redirect(url_for("index"))

    return render_template("hello.html", **context)


@app.errorhandler(404)
def not_found(error: object) -> object:
    return render_template("404.html", error=error)


@app.errorhandler(500)
def internal_server_error(error: object) -> object:
    return render_template("500.html", error=error)


@app.cli.command()
def test() -> None:
    tests = unittest.TestLoader().discover("tests")
    unittest.TextTestRunner().run(tests)
