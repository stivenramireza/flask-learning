from crypt import methods
from flask import render_template, session, flash, redirect, url_for

from src.auth.app import auth
from src.forms import LoginForm


@auth.route("/login", methods=["GET", "POST"])
def login() -> object:
    login_form = LoginForm()
    context = {"login_form": login_form}

    if login_form.validate_on_submit():
        username = login_form.username.data
        session["username"] = username

        flash("Username registered successfully")

        return redirect(url_for("index"))

    return render_template("login.html", **context)
