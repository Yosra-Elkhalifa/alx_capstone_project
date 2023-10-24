from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'smtp_username'

}

app.config.update(mail_settings)
mail = Mail(app)

if __name__ == '__main__':
    app.run(debug=True)
    with app.app_context():
        msg = Message(subject="Hello",
                      sender=app.config.get("MAIL_USERNAME"),
                      recipients=["yosra.osman93@gmail.com"], 
                      body="This is a test email I sent with Gmail and Python!")
        mail.send(msg)

