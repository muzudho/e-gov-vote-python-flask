from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return render_template('voted.html', bestmove=request.form['bestmove'])
    else:
        return '''<html>
<head>
    <title>電子政府きふわらべ</title>
</head>
<body>
    <img src="static/img/20211102shogi18.png"/><br/>
    <form method="POST">
        <input type="text" name="bestmove"/>
        <input type="submit" value="Vote!"/>
    </form>
</body>
</html>
'''