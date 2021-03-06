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
from wtforms.fields.html5 import DecimalRangeField

from threading import Thread, Lock
# from hksSer import serThread
import time
import bslCtrClient

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)
moment = Moment(app)
manager = Manager(app)

class ControlForm(FlaskForm):
    gid = IntegerField("Group Id:   ",[validators.Required("Please enter number.")])
    # pid = IntegerField("Private Id: ",[])
    pid = IntegerField("Private Id: ",[validators.Required("Please enter number.")])
    level = IntegerField("Level:     ",[validators.Required("Please enter number.")])

    # changed_gid = IntegerField("Change Group Id:   ",[validators.Required("Please enter number.")])
    # changed_pid = IntegerField("Change Private Id: ",[validators.Required("Please enter number.")])

    network = RadioField('Network', choices=[('0','T0'),
    ('1','T1'), ('2','T2'), ('3','T3'), ('4','T4')])

    rxtx = RadioField('Destination RxTx', choices=[('1','Rx'),
    ('2','Tx'), ('4','SRx'), ('32','Gateway')])

    # sub = RadioField('Command', choices=[('103','Control'), ('108','GroupChange'),
    # ('104','AutoMode'), ('109','Alternative'), ('102','Monitor'), ('110','Status'), ('101','Power')])
    sub = RadioField('Command', choices=[('103','Control'),
    ('104','AutoMode'), ('109','Alternative'), ('102','Monitor'), ('110','Status'), ('101','Power')])

    age = DecimalRangeField('Age', default=0)

    submit = SubmitField("Send")

    # subDict = dict([('103','Control'), ('108','GroupChange'),
    # ('104','AutoMode'), ('109','Alternative'),
    # ('102','Monitor'), ('110','Status'), ('101','Power')])

    subDict = dict([('103','Control'),
    ('104','AutoMode'), ('109','Alternative'),
    ('102','Monitor'), ('110','Status'), ('101','Power')])

    # rxtxDict = dict([('1','Rx'),
    # ('2','Tx'), ('4','SRx'), ('16','Repeat'), ('32','Gateway'), ('64','Master')])
    rxtxDict = dict([('1','Rx'),('2','Tx'), ('4','SRx'), ('32','Gateway')])

def FileSave(filename,content):
    import io
    with open(filename, "a+") as myfile:
        myfile.write(content)

def returnSubLabel(sub):
    form = ControlForm()
    return form.subDict[sub]

myFrame = Frame()

from datetime import datetime
@app.route('/', methods=['GET', 'POST'])
def control():
    form = ControlForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            print('form.validate() == False:')
            return render_template('control.html', form=form)
        else:
            # myFrame = Frame()
            global myFrame
            gid = request.form['gid']
            pid = request.form['pid']
            level = request.form['level']

            network = request.form['network']
            rxtx = request.form['rxtx']
            sub = request.form['sub']

            dt = datetime.now()
            print(dt.date(), dt.time())

            print('gid:{}, pid:{}, net:{} level:{}, rxtx:{}, sub:{}'.format(gid, pid, network,
            level, form.rxtxDict[rxtx], form.subDict[sub]))
             # returnSubLabel(sub)))
            writeStr = 'Send:: ' + str(dt.date()) + ':' + str(dt.time())
            writeStr += '--->gid:{}, pid:{}, level:{}, sub:{}'.format(gid, pid, level, returnSubLabel(sub))
            FileSave('send.txt', writeStr+'\n')

            # if(form.subDict[sub] == 'GroupChange'):
            #     cGid = int(request.form['changed_gid'])
            #     cPid = int(request.form['changed_pid'])
            #     cRxTx = int(rxtx)
            #     # cRxTx = int(request.form['changed_rxtx'])
            #     print('Now Group Change')
            #     myFrame.rate[0] = cPid; myFrame.status[0] = cRxTx;
            #     myFrame.level[0] = cGid%256; myFrame.Type[0] = int(cGid/256);
            # else:
            myFrame.rate[0] = 1; myFrame.status[0] = 0;
            myFrame.Type[0] = 1;
            myFrame.level[0]= int(level);
            myFrame.micom[0] = int(network);
            myFrame.rxtx[0] = int(rxtx); myFrame.sub[0] = int(sub)
            myFrame.gid[0] = int(gid); myFrame.pid[0] = int(pid);
            myFrame.setFrame()
            print('------------ Ctr Start ----------------')
            bslCtrClient.sendSocket(myFrame.getFrame())

            flash('Result::'+bslCtrClient.returnPowerOrStatus)
            flash('Add:'+bslCtrClient.returnMac)
            # mySer.send(myFrame.getFrame())
            print('------------ Ctr End ----------------')
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
