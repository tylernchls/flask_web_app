from flask import render_template, flash, redirect, request, url_for
from app import app, db
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse

@app.route('/')

@app.route('/index')
# protects this route until user is authenticated
@login_required
# View function that executes when route is hit
# Uses jinja template engine to inject dynamic content into templates
def index():
    return render_template('index.html', title='XXXXXXXXXXX')


@app.route('/login', methods=['GET', 'POST'])
def login():
    # redirect to index page if already logged in
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()

    if form.validate_on_submit():
        # query database for username that was submitted in form and return user object if exists
        user = User.query.filter_by(username=form.username.data).first()

        # redirects if username doesn't exist or password incorrect. Uses check_password method from user model
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password HAHA')
            return redirect(url_for('login'))

        # if both username and password are correct, calls login_user() from flask-login.
        # will register user as logged in, will have current_user variable set and redirect.
        login_user(user, remember=form.remember_me.data)
        
        # Will handle redirect to page user tried accessing before authentication
        # next value is appended to the url
        next_page = request.args.get('next')

        # Ensures that malicous url cant be inserted into next argument
        # Application only redirects using when url is relative,
        # using url_parse() function and then check if the netloc component is set or not.
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)

        return redirect(url_for('index'))
    
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, I just pawned your computer BAHAHAHA!')
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)