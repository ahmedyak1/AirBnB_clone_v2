#!/usr/bin/python3
"""program that launches a Flask online application""”

from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    """display "Hello HBNB!"

    Returns:
        str: text index page
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb_route():
    """display "HBNB"

    Return str: string  on the page
    """
    return 'HBNB'


@app.route('/c/<text>')
def c_route(text):
    """display "C", followed by the value of the text variable

    Args:string to be served on the page

    Return str on the page
    """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python_route(text):
    """display "Python", followed by the value of the text variable

    Args: string to be served on the page

    Return  text on the page
    """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number_route(n):
    """display "n is a number" only if n is an integer

    Args: number to be showed on page

    Return string on the page
    """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def number_template_route(n):
    """display a HTML page only if n is an integer

    Arg number to be displayed on page

    Return: string text on the page
    """
    return render_template('5-number.html', num=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even_route(n):
    """display a ftml

    Args: number to be showed on page

    Return :text on the page
    """
    if n % 2 == 0:
        condition = 'even'
    else:
        condition = 'odd'
    return render_template('6-number_odd_or_even.html', n=n,
                           condition=condition)


if __name__ == '__main__':
    app.run(debug=True)
