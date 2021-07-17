from app import app

import os
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
  return "Hello, World!"


