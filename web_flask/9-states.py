#!/usr/bin/python3
"""program that launches a Flask online application"""



from flask import Flask, render_template

from models import storage

# create an instance called app of the class by passong the __name__ variable
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_db(exception=None):
    """delete the curr SQLAlchemy Session
    """
    if storage is not None:
        storage.close()


@app.route('/states')
@app.route('/states/<state_id>')
def states(state_id=None):
    """shows a HTML pag inside the tag body"""
    states = storage.all("State")
    if state_id is None:
        return render_template('9-states.html', states=states)
    state = states.get('State.{}'.format(state_id))
    return render_template('9-states.html', state=state)


if __name__ == '__main__':
    app.run(debug=True)

