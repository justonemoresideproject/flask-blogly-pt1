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
    users = User.query.all()
    return render_template('homepage.html', users=users)

@app.route('/addNewUser')
def newUser():
    """Directs to add user page"""
    return render_template('newUser.html')

@app.route('/addedUser', methods=['POST'])
def addedUser():
    """Adds new user"""
    # first = request.args['first']
    # last = request.args.get['last']
    # url = request.args.get['image']

    # Taken from solution
    new_user = User(
        first_name=request.form['first'],
        last_name=request.form['last'],
        image_url=request.form['image'] or None)

    db.session.add(new_user)
    db.session.commit()

    return redirect('/')