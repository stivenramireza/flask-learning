from flask import Flask, request, make_response, redirect, render_template, session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config["SECRET_KEY"] = "SUPER SECRET"

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


@app.route("/hello")
def hello() -> object:
    user_ip = session.get("user_ip")
    login_form = LoginForm()
    context = {"user_ip": user_ip, "todos": todos, "login_form": login_form}
    return render_template("hello.jinja", **context)


@app.errorhandler(404)
def not_found(error: object) -> object:
    return render_template("404.jinja", error=error)


@app.errorhandler(500)
def internal_server_error(error: object) -> object:
    return render_template("500.jinja", error=error)
