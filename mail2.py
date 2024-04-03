import smtplib

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('samrig25@gmail.com', '')
    
    recipient = ''
    subject = 'Test Email'
    body = 'Hello there! This is a test email.'

    message = f'Subject: {subject}\n\n{body}'
    server.sendmail('', [''], message)
    
    print('Mail sent successfully!')
except Exception as e:
    print(f'Error sending email: {str(e)}')
finally:
    server.quit()  # Make sure to close the SMTP connection
