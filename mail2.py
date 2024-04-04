import smtplib


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('samrig25@gmail.com', 'irnc kkpy gnfs mwga')
    
recipient = 'benyas1asnake@gmail.com'
subject = 'Test Email'
body = 'Hello there! This is a test email. You have successfully registered.'

message = f'Subject: {subject}\n\n{body}'
try:
    server.sendmail('samrig25@gmail.com', ['benyas1asnake@gmail.com'], message)
    
    print('Mail sent successfully!')
except Exception as e:
    print(f'Error sending email: {str(e)}')
finally:
    server.quit()  # Make sure to close the SMTP connection
