from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
import string
import random

app = Flask(__name__)

# Configure SQLite database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "urls.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class ShortUrl(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500), nullable=False)
    short_code = db.Column(db.String(10), unique=True, nullable=False)
    clicks = db.Column(db.Integer, default=0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.short_code = self.generate_short_code()

    def generate_short_code(self):
        characters = string.ascii_letters + string.digits
        while True:
            short_code = "".join(random.choice(characters) for _ in range(6))
            if not ShortUrl.query.filter_by(short_code=short_code).first():
                return short_code


# Create tables
with app.app_context():
    db.create_all()


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        original_url = request.form["url"]
        if not original_url.startswith(("http://", "https://")):
            original_url = "http://" + original_url

        existing_url = ShortUrl.query.filter_by(original_url=original_url).first()

        if existing_url:
            short_url = request.host_url + existing_url.short_code
        else:
            new_url = ShortUrl(original_url=original_url)
            db.session.add(new_url)
            db.session.commit()
            short_url = request.host_url + new_url.short_code

        return render_template("index.html", short_url=short_url)

    return render_template("index.html")


@app.route("/<short_code>")
def redirect_to_url(short_code):
    url = ShortUrl.query.filter_by(short_code=short_code).first_or_404()
    url.clicks += 1
    db.session.commit()
    return redirect(url.original_url)


@app.route("/stats")
def stats():
    urls = ShortUrl.query.order_by(ShortUrl.clicks.desc()).all()
    return render_template("index.html", urls=urls)


if __name__ == "__main__":
    app.run(debug=True)
