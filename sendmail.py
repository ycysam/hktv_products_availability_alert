import smtplib
from email.mime.text import MIMEText
from email.header import Header
from datetime import datetime
from dotenv import dotenv_values

def send_alert(chi_name, link):
    config = dotenv_values('.env')
    GMAIL_APP_KEY = config["GMAIL_APP_KEY"]
    my_email = config["RECEIVER_EMAIL"]
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(config['SENDER_GMAIL'], GMAIL_APP_KEY)
    subject = chi_name
    message = MIMEText(link, 'plain', 'utf-8')
    message['From'] = Header('HKTV Alert Bot', 'utf-8')
    message['To'] = Header(my_email, 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')
    server.sendmail(
        my_email,
        my_email,
        message.as_string()
    )
    print('email sent.', datetime.now())
    server.quit()