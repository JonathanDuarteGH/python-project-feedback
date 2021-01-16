import smtplib
from email.mime.text import MIMEText


def send_mail(customer, dealer, rating, comments):
    smtpServer = 'smtp.mailtrap.io'
    port = 2525
    login = '761d4679a702d7'
    password = '8e7ec645c532bf'
    message = f"<h3>New Feedback Submission</h3><ul><li>Customer: {customer}</li><li>Dealer: {dealer}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>"

    sender_email = 'email1@example.com'
    receiver_email = 'email2@example.com'
    msg = MIMEText(message, 'html')
    msg['Submit'] = 'Tesla Feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send email
    with smtplib.SMTP(smtpServer, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
