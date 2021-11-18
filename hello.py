from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return render_template('voted.html', bestmove=request.form['bestmove'])
    else:
        return render_template('vote.html')