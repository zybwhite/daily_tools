import smtplib
import os
import base64
from email.mime.text import MIMEText


def send_email(msg_subject, msg_body="Refer to Subjects",
               from_addr='zybwhite.trading@gmail.com',
               to_addrs=['zybwhite.trading@gmail.com']):

    msg = """Content-Type: text/plain; charset="us-ascii"
MIME-Version: 1.0
Content-Transfer-Encoding: 7bit
From: {from_addr}
To: {to}
Subject: {subject}

{body}""".format(from_addr=(from_addr), to=','.join(to_addrs), subject=str(msg_subject), body=str(msg_body))

    username = from_addr
    try:
        password = base64.b64decode(os.environ['EMAIL_PASSWORD'])
    except KeyError:
        raise KeyError("No Password Found")

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(username, password)
    server.sendmail(from_addr, to_addrs, msg)
    server.quit()
    print "Email is sent!"

if __name__ == "__main__":
    send_email("Hello Huge", "Hello~~~")