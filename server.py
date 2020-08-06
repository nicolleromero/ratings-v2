"""Server for movie ratings app."""

from flask import Flask, render_template

app = Flask(__name__)


# Replace this with routes and view functions!
@app.route("/")
def homepage():
    return render_template("base.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
