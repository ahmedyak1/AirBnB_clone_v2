#!/usr/bin/python3
"""program that launches a Flask online application"""

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def index():
    """display "Hello HBNB!"
        str: text on index page
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb_route():

    """display "HBNB"
        str: text  page
    """
    return 'HBNB'


@app.route('/c/<text>')
def c_route(text):
    """display "C", followed by the value of the text variable

    Args:
        text (str): text to be served on the page

    Returns:
        str: text  page
    """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python_route(text):
    """display "Python", followed by the value of the text variable


    Args:
        text (str): text to be served on the page
        str: text on page
    """
    return 'Python {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(debug=True)
