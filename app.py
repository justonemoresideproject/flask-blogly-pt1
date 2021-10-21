"""Blogly application."""
from flask import Flask, request, redirect, render_template
# from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

# THIS VARIABLE
users = User.query.order_by(User.last_name, User.first_name).all()

@app.route('/')
def homepage():
    """Shows all users"""
    # SHOULD PASS TO THIS VARIABLE, THEN  TO THE VARIABLE IN THE PARENTHESES
    users = users
    return render_template('homepage.html', users=users)

@app.route('/addNewUser')
def newUser():
    """Directs to add user page"""
    return render_template('newUser.html')

@app.route('/addedUser', methods=['POST'])
def addedUser():
    """Adds new user"""
    new_user = User(
        first_name=request.form['first'],
        last_name=request.form['last'],
        image_url=request.form['image'] or None)

    db.session.add(new_user)
    db.session.commit()

    return redirect('/')

@app.route('/editUser/<id>')
def editUser(id):
    """Edits a user by requesting a value from 0 to # of users. Then passes that value and to editUser.html to request the correct information."""

    user = User.query.order_by(User.id).all()[int(id) - 1]

    return render_template('editUser.html', user=user)

@app.route('/commit/<id>')
def commitChanges(id):
    changedUser = User.query.order_by(User.id).all()[int(id)]
    changedUser.first_name = request.form['first']
    changedUser.last_name = request.form['last']
    changedUser.image_url = request.form['image']

    db.session.add(changedUser)
    db.session.commit()

    return redirect('/')