# Project Hello Flask #
from flask import Flask

app = Flask(__name__)

# use decorators to link the function to the url
@app.route("/")
@app.route("/hello")

# define the view using a function to return a string
def hello_world():
	return "Hello, World!"

if __name__ == "__main__":
	app.run()
