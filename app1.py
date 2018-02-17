from flask import Flask

# create Instance of Flask object using module name.
app = Flask(__name__)


# Decorator for URL routing.
@app.route("/")
def index():
    return "Hello, World!"

if __name__ = '__main__':
    app.run(port=5000, debug=True)