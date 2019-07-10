from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Goluxas'}
    posts = [
            {
                'author': {'username': 'John'},
                'body': 'Beautiful day in Portland!',
            },
            {
                'author': {'username': 'Susan'},
                'body': 'The blackout is a pain though...',
            }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
