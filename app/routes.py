from flask import render_template, flash, redirect, request, url_for
from app import app, db
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required, UserMixin
from app.models import User
from werkzeug.urls import url_parse


@app.route('/')
@app.route('/index')
@login_required
def index():
    user = {'username': 'Jacques'}
    posts = [
        {
            'author': {'username': 'Megan'},
            'body':	'Isn\'t Newport a beautiful place!'
        },
        {
            'author': {'username': 'Boo'},
            'body':	'I love my new owners!'
        },
        {
            'author': {'username': 'Jerry'},
            'body':	'I\'ve gone feral👿! '
        },
        {
            'author': {'username': 'Dave'},
            'body':	'What on earth should I do with my life now that my dissertation is done?'
        }
    ]

    # render_template used to change html pages.
    return render_template('index.html', title='Home Page', posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))

        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')

        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')

        return redirect(next_page)

    return render_template('login.html', title='Sign In', form=form)

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
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


# <> in the route url is dynamic
# flask will accept any text in that 
# invokes view function with text as argument
@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author':user, 'body': 'Test post #1'},
        {'author':user, 'body': 'Test post #1'}
    ]
    return render_template('user.html', user=user, posts=posts)


# This modifies the test view function with a decorator
# The @app.route decorator creates an association between the argument URL and the function.
@app.route('/test')
@app.route('/davetest')
def test():
    return 'Testing to see if this works'
