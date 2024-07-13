import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email details
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_USERNAME = 'elayarajameenaloshini002@gmail.com'
SMTP_PASSWORD = 'rxjl uxdw qyjm tvow'
FROM_EMAIL = 'elayarajameenaloshini002@gmail.com'
TO_EMAILS = [
    'muflihayounus@gmail.com',
    'sit20ad009@sairamtap.edu.in',
    'btechcce210095@smvec.ac.in',
    'sit20ad051@sairamtap.edu.in',
    'jaswanth.mathan@gmail.com',
    'sec21cb009@sairamtap.edu.in',
    'vijayasubash.e@gmail.com',
    'samimayounus@gmail.com',
    'sugunaelayaraja@gmail.com',
    'aswinsiva2k@gmail.com',
    'muflihayounus@gmail.com',
    'sit20ad009@sairamtap.edu.in',
    'btechcce210095@smvec.ac.in',
    'sit20ad051@sairamtap.edu.in',
    'jaswanth.mathan@gmail.com',
    'sec21cb009@sairamtap.edu.in',
    'vijayasubash.e@gmail.com',
    'samimayounus@gmail.com',
    'sugunaelayaraja@gmail.com',
    'aswinsiva2k@gmail.com'
]
SUBJECT = 'Test Email'
BODY = 'This is a test email.'

# Function to send email
def send_email(smtp_server, smtp_port, smtp_username, smtp_password, from_email, to_emails, subject, body):
    try:
        # Set up the server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)

        # Create the email
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = ", ".join(to_emails)
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Send the email
        server.sendmail(from_email, to_emails, msg.as_string())
        server.quit()
        print(f"Email sent successfully to {', '.join(to_emails)}.")
    except Exception as e:
        print(f"Failed to send email to {', '.join(to_emails)}: {str(e)}")

# Send emails in batches of 10 with a 5-minute delay between batches
batch_size = 10
for i in range(0, len(TO_EMAILS), batch_size):
    batch = TO_EMAILS[i:i + batch_size]
    send_email(SMTP_SERVER, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD, FROM_EMAIL, batch, SUBJECT, BODY)
    if i + batch_size < len(TO_EMAILS):  # Avoid waiting after the last batch
        print("Waiting for 5 minutes before sending the next batch of emails...")
        time.sleep(300)
