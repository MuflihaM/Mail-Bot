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
TO_EMAIL = 'sit20ad009@sairamtap.edu.in'
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
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")

# Send 20 emails with a gap of 1 minute
for i in range(20):
    if i == 10:
        # Pause for 1 hour after sending 10 emails
        print("Pausing for 1 hour after sending 10 emails...")
        time.sleep(3600)
    send_email(SMTP_SERVER, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD, FROM_EMAIL, TO_EMAIL, SUBJECT, BODY)
    print(f"Email {i + 1} sent.")
    if i != 19:  # Avoid waiting after the last email
        time.sleep(60)
