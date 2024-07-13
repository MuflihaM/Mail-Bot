import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Load the Excel file
file_path = r'C:\Data\Mail Merge Sheet .xlsx'  # Note the 'r' before the string for raw string literal
sheet1_data = pd.read_excel(file_path, sheet_name='Sheet1')

# Extract the relevant columns
email_data = sheet1_data[['Company Name', 'First Name', 'Last Name', 'Mail ID']]

# Define the email template
email_template = """\
<html>
  <body style="font-family: Arial, sans-serif;">
    <p style="color: black;">

      Hi {First_Name} {Last_Name},<br><br>
      {Company_Name}<br><br>

      <u>Reference:</u> Data Driven Insights to Understand the Indian Fintech SaaS / Financial Software Market Market Opportunity.<br><br>
      How much Money the Indian ID Verification Companies, Fraud Prevention Companies, Alternate Data, AML Companies and Core Banking companies Make?<br><br>

      <u>Why am I Reaching out to {First_Name}?</u><br><br>

      &emsp1. Did a Financial Health Analysis of the Companies Operating in the Financial Software, ID Verification, Fraud Prevention, Payment Fintech & Fintech SaaS Space in India.<br>

      &emsp2. I have <b><span style="color: red;"> Mapped a Whooping 🙄 613 Companies</span></b>. Revenue is mapped for 6 Financial Years (Key Metrics like EBITDA Margin, Net Margin & ROCE are compared)<br>

      &emsp3. As the Industry is heading towards Mergers and Acquisitions, These Metrics and Analysis will be extremely useful in <b>devising the right Strategy.</b><br><br>

      <u>Why You Shouldn't be Ignoring this Detailed Fintech SaaS Market Analysis?</u><br><br>

      &emsp1. I have <b>attached a Document which contains <span style="color: red;">167 Questions</span></b> - Please go through the questions thoroughly, we can share the detailed analysis with you.<br>

      &emsp2. There are some Interesting Companies in the Analysis. You will have an Opportunity to look at the Size of the Fintech SaaS Market and how fast it's growing.<br><br>

      ✅100% this Analysis will <b>Supercharge your Strategy & Decision Making.</b><br><br>

      Please let me know when is the right time to connect with Your team and showcase the Value you can extract from this Analysis.<br><br>

      Eagerly Looking forward to your Response.<br><br>

      Thanks<br>
      Karthik Kannan R<br>
      <a href="https://www.linkedin.com/in/karthik-kannan-ravi-544a918">LinkedIn</a><br>
      Phone - 9944865029<br>
    </p>
  </body>
</html>
"""

# Email credentials and server settings
your_email = "elayarajameenaloshini002@gmail.com"
your_password = "rxjl uxdw qyjm tvow"  # Use environment variables or secure methods to handle this
smtp_server = "smtp.gmail.com"
smtp_port = 587  # or 465 for SSL

# Create an SMTP session
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()  # Enable security
server.login(your_email, your_password)

# Send the emails
for index, row in email_data.iterrows():
    # Create the email content
    email_content = email_template.format(
        Mail_ID=row['Mail ID'],
        Company_Name=row['Company Name'],
        First_Name=row['First Name'],
        Last_Name=row['Last Name']
    )
    
    # Create a MIME object
    msg = MIMEMultipart()
    msg['From'] = your_email
    msg['To'] = row['Mail ID']
    msg['Subject'] = f"{row['Company Name']}<> Indian Fintech SaaS Market Analysis. (ID Verification Companies)"
    msg.attach(MIMEText(email_content, 'html'))

    # Attach file
    attachment = open(r'C:\Data\Financial Health Analysis_1.pdf', 'rb')  # Replace with your file path
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= " + 'Financial Health Analysis_1.pdf')  # Replace with your file name
    msg.attach(part)
    
    # Send the email
    server.sendmail(your_email, row['Mail ID'], msg.as_string())
    print(f"Email sent to {row['Mail ID']}")

# Terminate the SMTP session
server.quit()
