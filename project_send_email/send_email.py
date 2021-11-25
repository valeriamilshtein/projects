import smtplib  # Handles different parts of the protocol: connecting, authenticating, validation, sending emails.
from datetime import datetime  # Supplies classes for manipulating dates and times.

gmail_account = {
    'user': 'valeriiapidpala@gmail.com',
    'password': 'mypassword',
    'recipients': ['valeriamilshtein@gmail.com', 'kartoshka548@gmail.com']
}

sent_from = gmail_account['user']
to = gmail_account['recipients']
subject = 'Super Important Message'
body = '''
Hey, I did it!!!
You asked me about current date... Here we are: 
''' + datetime.today().strftime('%Y-%m-%d-%H:%M:%S')

email_text = '''\
From: %s
To: %s
Subject: %s

%s
''' % (sent_from, ', '.join(to), subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_account['user'], gmail_account['password'])
    server.sendmail(sent_from, to, email_text)
    server.close()

    print('Email sent!')  # If success
except:
    print('Something went wrong!')  # If error