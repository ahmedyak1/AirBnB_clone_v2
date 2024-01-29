#!/usr/bin/python3
"""program that launches a Flask online application"""

from flask import Flask, render_template

from models import storage


# create an instance called app of the class by passong the __name__ variable
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_db(exception=None):
    """removes current session
    """
    if storage is not None:
        storage.close()


@app.route('/cities_by_states')
def cities_list(n=None):
    """shows a HTML page inside the tag booody"""



    statess = storage.all('State').values()
    return render_template('8-cities_by_states.html', states=statess)


if __name__ == '__main__':
    app.run(debug=True)

