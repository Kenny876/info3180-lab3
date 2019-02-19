from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'moneymoneymoney'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '465' # (or try 2525)
app.config['MAIL_USERNAME'] = '991ad73e458c25'
app.config['MAIL_PASSWORD'] = '5c73111cbee627'
mail = Mail(app)

from app import views




