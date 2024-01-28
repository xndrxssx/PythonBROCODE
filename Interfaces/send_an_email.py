import smtplib

sender = "acarvalho0710@gmail.com"
receiver = "luyza2012@live.com"
password = "hyoyeon88"
subject = "Teste Python"
body = "Programa em Python que envia e-mail :D"

message = f"""From: {sender}
To: {receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:
    server.login(sender, password)
    print("Logged in...")
    server.sendmail(sender, receiver, message)
    print("Email has been sent")
except smtplib.SMTPAuthenticationError:
    print("Unable to sign in")