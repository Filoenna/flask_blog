from flask import Flask, render_template, flash, redirect
from flask.helpers import url_for
from forms import RegistrationForm, LoginForm

import os
from dotenv import load_dotenv

load_dotenv()
secret_key = os.getenv("SECRET_KEY")


app = Flask(__name__)
app.config["SECRET_KEY"] = secret_key

posts = [
    {
        "author": "Corey Schafer",
        "title": "Blog post 1",
        "content": "First post content",
        "date_posted": "April 20, 2021",
    },
    {
        "author": "Jane Doe",
        "title": "Blog post 2",
        "content": "Second post content",
        "date_posted": "April 21, 2021",
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True)
