from flask import render_template
from app import app

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


# This modifies the test view function with a decorator
# The @app.route decorator creates an association between the argument URL and the function.
@app.route('/test')
@app.route('/davetest')
def test():
	return 'Testing to see if this works'