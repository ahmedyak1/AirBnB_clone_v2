#!/usr/bin/python3
"""Program that launches a Flask online application"""


from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    """display "Hello HBNB!"

    Returns:
        str: str pageee
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb_route():
    """display "HBNB"

    Return 
        str str page 
    """
    return 'HBNB'


if __name__ == '__main__':
    app.run(debug=True)
