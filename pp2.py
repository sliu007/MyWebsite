import smtplib
import ssl

def send_email_topic(message):
    host = "smtp.gmail.com"
    port = 465

    username = "samdamanthatlikesham@gmail.com"
    password = "ybwhjebwkrosnjkt"

    receiver = "samdamanthatlikesham@gmail.com"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
