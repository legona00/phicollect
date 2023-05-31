import smtplib
from email.mime.text import MIMEText

#Function to send an email to a brother whenever they incurr a new sanction
def send_email(body, recipient):
    msg = MIMEText(body)
    msg['Subject'] = 'Sanction Statement'
    msg['From'] = 'tamufiastandards@gmail.com'
    msg['To'] = recipient
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.login('tamufiastandards@gmail.com', 'gyuzycqennoagtse')
    smtp_server.sendmail('tamufiastandards@gmail.com', recipient, msg.as_string())
    smtp_server.quit()