"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

# Replace this with routes and view functions!
@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/users', methods=['POST'])
def register_user():
    """Create a new user."""
    
    email = request.form.get('email')
    password = request.form.get('password')

    if crud.get_user_by_email(email):
        flash('Cannot create an account with that email. Try again.')
    else:
        crud.create_user(email, password)
        flash('Account created successfully. Please log in.')

    return redirect('/')

    

@app.route('/movies')
def show_all_movies():
    movies = crud.get_movies()

    return render_template('all_movies.html', movies=movies)

@app.route('/movies/<movie_id>')
def show_movie(movie_id):

    movie = crud.get_movie_by_id(movie_id)
    return render_template('movie_details.html', movie=movie)

@app.route('/users')
def show_all_users():
    users = crud.get_users()
    return render_template('all_users.html', users=users)

@app.route('/users/<user_id>')
def show_user(user_id):

    user = crud.get_user_by_id(user_id)
    return render_template('users_details.html', user=user)

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
