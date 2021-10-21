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

@app.route('/')
def homepage():
    """Shows all users"""
    users = User.query.order_by(User.last_name, User.first_name).all()
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

@app.route('/editUser/<user_id>')
def editUser(user_id):
    """Edits a user by requesting a value from 0 to # of users. Then passes that value and to editUser.html to request the correct information."""

    # user = User.query.order_by(User.last_name, User.first_name).all()[int(id) - 1]
    user = User.query.get_or_404(user_id)

    return render_template('editUser.html', user=user)

@app.route('/commit/<user_id>')
def commitChanges(user_id):
    # changedUser = User.query.order_by(User.last_name, User.first_name).all()[int(id) - 1]
    changedUser = User.query.get_or_404(int(user_id))
    changedUser.first_name = request.args['first']
    changedUser.last_name = request.args['last']
    changedUser.image_url = request.args['image']

    db.session.add(changedUser)
    db.session.commit()

    return redirect('/')