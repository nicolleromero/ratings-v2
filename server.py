"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def homepage():
    """View homepage"""

    return render_template("homepage.html")

@app.route("/movies")
def all_movies():
    """View all movies"""

    movies = crud.get_movies()

    return render_template("all_movies.html", movies=movies)


@app.route("/users")
def all_users():
    """View all users"""

    users = crud.get_users()

    return render_template("all_users.html", users=users)


@app.route('/movies/<movie_id>')
def show_movie(movie_id):
    """Show details of one movie"""

    movie = crud.get_movie_by_id(movie_id)

    return render_template('movie_details.html', movie=movie)


@app.route('/users/<user_id>')
def show_user(user_id):
    """Show details of one user"""

    user = crud.get_user_by_id(user_id)

    return render_template('user_details.html', user=user)


@app.route('/users', methods=['POST'])
def register_user():
    """Create a new user."""

    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)
    if user:
        flash('Cannot create an account with that email. Try again.')
    else:
        crud.create_user(email, password)
        flash('Account created! Please log in.')

    return redirect('/')

@app.route('/handle-login', methods=['POST'])
def handle_login():
    """Log user into application."""

    email = request.form['email']
    password = request.form['password']

    user = crud.get_user_by_email(email)

    if user == crud.get_user_by_password(password):
        flash(f'Logged in as {email}')
        session['current_user'] = user.user_id
        flash(f'User_id {user.user_id}')
        return redirect('/')

    else:
        flash('Wrong password!')
        return redirect('/')


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
