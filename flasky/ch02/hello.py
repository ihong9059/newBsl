from flask import Flask
from flask_script import Manager

app = Flask(__name__)

manager = Manager(app)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name


if __name__ == '__main__':
    # app.run(debug=True)
    manager.run()
# python3 hello.py runserver --host 0.0.0.0
