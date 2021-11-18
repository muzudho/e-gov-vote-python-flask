from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('enter.html')

@app.route('/vote', methods=['POST'])
def vote():
    yourName = request.form['yourName']
    # 長文送られても困るし適当にスライスしよ（＾～＾）
    yourName = yourName[0:20]
    # secret を難読にする時間がなかったので平文で埋め込み
    secret=request.form['secret']
    secret = secret[0:20]
    return render_template('vote.html',
                           yourName=yourName,
                           secret=secret)

@app.route('/thanks', methods=['POST'])
def thanks():
    yourName = request.form['yourName']
    yourName = yourName[0:20]
    secret=request.form['secret']
    secret = secret[0:20]
    m = request.form['bestmove']
    m = m[0:10]
    return render_template('thanks.html',
                           yourName=yourName,
                           secret=secret,
                           bestmove=m)

@app.route('/back', methods=['POST'])
def back():
    yourName = request.form['yourName']
    yourName = yourName[0:20]
    secret=request.form['secret']
    secret = secret[0:20]
    return render_template('vote.html',
                           yourName=yourName,
                           secret=secret)
