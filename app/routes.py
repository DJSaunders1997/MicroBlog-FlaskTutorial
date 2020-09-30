from app import app

@app.route('/')
@app.route('/index')
def index():
	return 'Hello, World!'

# This modifies the test view function with a decorator
# The @app.route decorator creates an association between the argument URL and the function.
@app.route('/test')
@app.route('/davetest')
def test():
	return 'Testing to see if this works'