from flask import Blueprint

app = Blueprint("general", __name__)


@app.route('/')
def main():
    return 'this is main page'


@app.route('/about')
def about():
    return 'about us'
