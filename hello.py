from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return '''<html>
<head>
    <title>電子政府きふわらべ</title>
</head>
<body>
    <img src="static/img/20211102shogi18.png"/><br/>
    ok
</body>
</html>
'''
        pass
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