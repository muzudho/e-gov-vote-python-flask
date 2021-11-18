from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('vote.html')

@app.route('/voted', methods=['POST'])
def voted():
    return render_template('voted.html', bestmove=request.form['bestmove'])
