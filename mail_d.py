from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
import hashlib
import secrets
import string
from datetime import datetime, timedelta

app = Flask(__name__)
"""
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///admin.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False"""

app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Update with your SMTP server
app.config['MAIL_PORT'] = 587  # Update with your SMTP port
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'samrig25@gmail.com'  # Update with your email credentials
app.config['MAIL_PASSWORD'] = 'irnckkpygnfsmwga'  # Update with your email credentials

mail = Mail(app)

def send_otp_email(username, otp):
    msg = Message('Password Reset OTP',sender='samrig25@gmail.com', recipients=[username])
    msg.body = f'Your OTP for password reset is: {otp}'
    mail.send(msg)

#endpoint
@app.route('/api/send_otp', methods=['POST'])
def send_otp():
    data = request.get_json()
    otp = ''.join(secrets.choice(string.digits) for i in range(6))
    send_otp_email(data['username'], otp)
    return {'otp': otp}
if __name__ == '__main__':
    #create_tables()
    app.run(debug=True)

