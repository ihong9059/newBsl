from flask import Flask, render_template, session, redirect
from flask import url_for, flash, request
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import TextField, IntegerField, TextAreaField
from wtforms import SubmitField, RadioField, SelectField
from wtforms import validators, ValidationError
from wtforms import StringField
from wtforms.validators import DataRequired
from flask_script import Manager
from frame import Frame

from threading import Thread, Lock
# from hksSer import serThread
import time
import bslCtrClient

app = Flask(__name__)

manager = Manager(app)

from datetime import datetime
@app.route('/', methods=['GET', 'POST'])
def control():
    return 'Nice to meet you'

if __name__ == '__main__':
    print('Now Run')
    # app.run(debug=True)
    manager.run()
# python3 hello.py runserver --host 0.0.0.0
# py bsl.py
