
import smtplib
from email.message import EmailMessage
import ssl #keeping internet connection secure

EMAIL_SUBJ      = "P5 email test"
EMAIL_BODY      = "Message sent from python code test"

email_sender    = "p5todosender@gmail.com"
pw_sender       = "Josh=confidant#1"
app_pw_sender   = 'yurrhlfmlpzmxfwp'
email_reciever  = "andreid3170@gmail.com"



em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciever

em['Subject'] = EMAIL_SUBJ
em.set_content(EMAIL_BODY)

# Security
contect = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contect) as smtp:
    smtp.login(email_sender, app_pw_sender)
    smtp.sendmail(email_sender, email_reciever, em.as_string())


# # https://stackoverflow.com/questions/16512592/login-credentials-not-working-with-gmail-smtp
# # NO LONGER WORKING... though

# import smtplib

# EMAIL_MSG = "Message sent from python code test"

# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.starttls()

# server.login("p5todosender@gmail.com", "Josh=confidant#1")
# server.sendmail("p5todosender@gmail.com", "andreid3170@gmail.com", EMAIL_MSG)
# print("mail sent!")


