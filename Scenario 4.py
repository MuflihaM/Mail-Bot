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
    'jaswanth.mathan@gmail.com'
]
SUBJECT = 'Test Email'
BODY = 'This is a test email.'

# Function to send email
def send_email(smtp_server, smtp_port, smtp_username, smtp_password, from_email, to_email, subject, body):
    try:
        # Set up the server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)

        # Create the email
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Send the email
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        print(f"Email sent successfully to {to_email}.")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {str(e)}")

# Send emails to the list with a delay of 30 minutes between each
for i, to_email in enumerate(TO_EMAILS):
    send_email(SMTP_SERVER, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD, FROM_EMAIL, to_email, SUBJECT, BODY)
    print(f"Email {i + 1} sent to {to_email}.")
    if i != len(TO_EMAILS) - 1:  # Avoid waiting after the last email
        print("Waiting for 30 minutes before sending the next email...")
        time.sleep(1800)
