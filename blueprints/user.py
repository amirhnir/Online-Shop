from flask import Blueprint

app = Blueprint("user", __name__)


@app.route('/user')
def user():
    return 'this is user page'
