from flask import Flask
from flask_mail import Mail, Message

app =Flask(__name__)
mail=Mail(app)

app.config['MAIL_SERVER']='smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'ihong9059@gmail.com'
app.config['MAIL_PASSWORD'] = 'Hongks@6063'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = True


@app.route("/")
def index():
    msg = Message(
        'Hello',
        sender='ihong@uttec.co.kr',
        recipients=['ihong9059@gmail.com'])
    msg.body = "This is the email body"
    mail.send(msg)
    return "Sent"

if __name__ == '__main__':
    app.run(debug=True)
