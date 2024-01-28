#!/usr/bin/python3
"""program that launches a Flask online application"""

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    """display "Hello HBNB!"

    Returns:
        str: text on the index page
    """
    return 'Hello HBNB!'

@app.route('/hbnb')
def hbnb_route():
    """display "HBNB"

    Returns:
        str: text on the page
    """
    return 'HBNB'


if __name__ == '__main__':
    app.run(debug=True)
