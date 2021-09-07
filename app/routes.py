
import os
from flask import render_template,flash,redirect,url_for,request
from flask import send_from_directory
from flask_login import login_user,logout_user,current_user,login_required
from werkzeug.urls import url_parse
from app import app,db
from app.forms import LoginForm,RegistrationForm
from app.models import User,Post

@app.route('/favicon.ico')
def favicon():
  return send_from_directory(
    os.path.join(app.root_path, 'images','icons','thinking'),
    'favicon-16x16.ico',
    mimetype='image/vnd.microsoft.icon'
  )

@app.route('/')
@app.route('/index')
@login_required
def index():
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
  return render_template('index.html',title='Home',posts=posts)

@app.route('/login',methods=['GET','POST'])
def login():
  if current_user.is_authenticated:
    return redirect(url_for('index'))
  form=LoginForm()
  if form.validate_on_submit():
    user=User.query.filter_by(username=form.username.data).first()
    if user is None or not user.check_password(form.password.data):
      flash("Invalid username or password.")
      return redirect(url_for('login'))
    login_user(user,remember=form.remember_me.data)
    next_page=request.args.get('next')
    if not next_page or url_parse(next_page).netloc!='':
      next_page=url_for('index')
    return redirect(next_page)
  return render_template('login.html',title='Sign In',form=form)

@app.route('/logout')
def logout():
  logout_user()
  return redirect(url_for('index'))

@app.route('/register',methods=['GET','POST'])
def register():
  if current_user.is_authenticated:
    return redirect(url_of('index'))
  form=RegistrationForm()
  if form.validate_on_submit():
    user=User(username=form.username.data,email=form.email.data)
    user.set_password(form.password.data)
    db.session.add(user)
    db.session.commit()
    flash("Congratulations! You're now a registered user. (It's time for your first login.)")
    return redirect(url_for('login'))
  return render_template('register.html',title='Register',form=form)

@app.route('/user/<username>')
@login_required
def user(username):
  user=User.query.filter_by(username=username).first_or_404()
  posts=[
    dict(author=user,body="Test post #1"),
    dict(author=user,body="Test post #2"),
  ]    
  return render_template('user.html',user=user,posts=posts)


