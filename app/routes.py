from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
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
			'body':	'What on earth should I do with my life now that my dissertation is done? '
		}
	]

	# render_template used to change html pages.
	return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash(f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}')
		return redirect('/index')
	return render_template('login.html', title='Sign In', form=form)

# This modifies the test view function with a decorator
# The @app.route decorator creates an association between the argument URL and the function.
@app.route('/test')
@app.route('/davetest')
def test():
	return 'Testing to see if this works'