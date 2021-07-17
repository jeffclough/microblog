from app import app

import os
from flask import render_template
from flask import send_from_directory

@app.route('/favicon.ico')
def favicon():
  return send_from_directory(
    os.path.join(app.root_path, 'images','icons','thinking'),
    'favicon-16x16.ico',
    mimetype='image/vnd.microsoft.icon'
  )

@app.route('/')
@app.route('/index')
def index():
  user=dict(username='Jeff')
  posts=[
    dict(
      author=dict(username='John'),
      body="Beautiful Day in Portland!",
    ),
    dict(
      author=dict(username='Susan'),
      body="The Avergers Movie Was So Cool!"
    ),
  ]
  return render_template('index.html',title='Home',user=user,posts=posts)
