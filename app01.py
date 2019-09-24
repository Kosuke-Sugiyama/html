from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def hello():
    return '<h1>Hello world<h1>'


@app.route('/goodbye')
def goodbye():
    return "Good bye"


@app.route('/add/<a>/<b>')
def add(a, b):
    return str(int(a) + int(b))


if __name__ == '__main__':
    app.run(debug=True, port=7777)
