from flask import Flask, url_for, request
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def hello_world():
    return ('Hello world')

@app.route('/about')
def view_about():
    return 'This is about route'

@app.route('/contact')
def view_contact():
    return 'This is contact route'

@app.route('/user/<string:username>') #convertor : string
def view_user(username: str):
    return username

@app.route('/items/<int:item_id>')
def read_item(item_id):
    return str(item_id)
    

@app.route('/path/<path:subpath>')
def get_subpath(subpath):
    return subpath

with app.test_request_context():
    print(url_for('view_contact'))
    print(url_for('read_item', item_id=15))
    print(url_for('view_user', username='SharmilaS'))
    print(url_for('static', filename='style.css'))
    print(url_for('view_contact', join='accepted'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if ( request.method == 'POST' ):
        return 'Login user' #if POST request
    else:
        return 'Show login form' #if GET request