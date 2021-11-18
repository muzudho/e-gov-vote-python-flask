from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/hello')
def hello():
    return '<img src="static/img/20211102shogi18.png" />'