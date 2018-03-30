from flask import Flask, render_template, session, redirect, url_for, flash, request
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
from hksSer import serThread
import time

mySer = serThread()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)
moment = Moment(app)
manager = Manager(app)

class ControlForm(FlaskForm):
    gid = IntegerField("Group Id:   ",[validators.Required("Please enter your name.")])
    pid = IntegerField("Private Id: ",[])
    # pid = IntegerField("Private Id: ",[validators.Required("Please enter your name.")])
    level = IntegerField("Level:     ",[])

    changed_gid = IntegerField("Change Group Id:   ",[validators.Required("Please enter your name.")])
    changed_pid = IntegerField("Change Private Id: ",[validators.Required("Please enter your name.")])

    rxtx = RadioField('Destination RxTx', choices=[('1','Rx'),
    ('2','Tx'), ('4','SRx'), ('32','Gateway')])

    changed_rxtx = RadioField('changed RxTx', choices=[('1','Rx'),
    ('2','Tx'), ('4','SRx'), ('32','Gateway')])


    sub = RadioField('Command', choices=[('103','Control'), ('108','GroupChange'),
    ('104','AutoMode'), ('109','Alternative'), ('102','Monitor'), ('110','Status'), ('101','Power')])

    submit = SubmitField("Send")
    subDict = dict([('103','Control'), ('108','GroupChange'),
    ('104','AutoMode'), ('109','Alternative'),
    ('102','Monitor'), ('110','Status'), ('101','Power')])

    rxtxDict = dict([('1','Rx'),
    ('2','Tx'), ('4','SRx'), ('16','Repeat'), ('32','Gateway'), ('64','Master')])

# @app.route('/start', methods=['GET', 'POST'])
def startSer():
    form = ControlForm()
    if mySer.serFirstFlag:
        mySer.serFirstFlag = False
        mySer.start()
        print('Now start my Serial')
        time.sleep(1)
    return render_template('control.html', form=form)

def FileSave(filename,content):
    import io
    with open(filename, "a+") as myfile:
        myfile.write(content)

def returnSubLabel(sub):
    form = ControlForm()
    return form.subDict[sub]

from datetime import datetime
@app.route('/', methods=['GET', 'POST'])
def control():
    startSer()
    form = ControlForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            print('form.validate() == False:')
            return render_template('control.html', form=form)
        else:
            myFrame = Frame()
            gid = request.form['gid']
            pid = request.form['pid']
            level = request.form['level']

            rxtx = request.form['rxtx']
            sub = request.form['sub']

            dt = datetime.now()
            print(dt.date(), dt.time())
            if(form.subDict[sub] == 'GroupChange'):
                cGid = int(request.form['changed_gid'])
                cPid = int(request.form['changed_pid'])
                cRxTx = int(request.form['changed_rxtx'])
                print('Now Group Change')
                myFrame.rate[0] = cPid; myFrame.status[0] = cRxTx;
                myFrame.dtime[0] = cGid;

            print('gid:{}, pid:{}, level:{}, rxtx:{}, sub:{}'.format(gid, pid, level,
             form.rxtxDict[rxtx], form.subDict[sub]))
             # returnSubLabel(sub)))
            writeStr = 'Send:: ' + str(dt.date()) + ':' + str(dt.time())
            writeStr += '--->gid:{}, pid:{}, level:{}, sub:{}'.format(gid, pid, level, returnSubLabel(sub))
            FileSave('send.txt', writeStr+'\n')

            myFrame.setGid(int(gid)); myFrame.setPid(int(pid)); myFrame.setLevel(int(level));
            myFrame.setRxTx(int(rxtx)); myFrame.setSub(int(sub))
            myFrame.setFrame()
            mySer.send(myFrame.getFrame())
            return render_template('control.html', form=form)

    elif request.method == 'GET':
        print('request.method == GET ')
        return render_template('control.html', form=form)

if __name__ == '__main__':
    print('Now Run')
    # app.run(debug=True)
    manager.run()
# python3 hello.py runserver --host 0.0.0.0
# py bsl.py
