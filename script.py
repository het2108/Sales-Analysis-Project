# import pandas as pd
# import smtplib
# import time
# from jinja2 import Template
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

# # SMTP credentials
# EMAIL_ADDRESS = "hetthakkar158@gmail.com"
# EMAIL_PASSWORD = "hoot svip bzgt apil"
# SMTP_SERVER = "smtp.gmail.com"
# SMTP_PORT = 587

# # Load Excel and HTML template
# df = pd.read_excel("cleaned_agency_list.xlsx")
# with open("email_template.html", "r") as file:
#     html_template = Template(file.read())

# # Setup SMTP connection
# server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
# server.starttls()
# server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

# batch_size = 10  # Emails per batch
# delay_between_emails = 10  # seconds
# delay_between_batches = 60  # seconds

# emails_sent = 0

# for index, row in df.iterrows():
#     if pd.isna(row.get("Email")):
#         continue

#     recipient_email = row["Email"]
#     contact_person = row.get("Contact Person", "there")
#     company_name = row.get("Company Name", "your company")

#     # Prepare personalized email content
#     html_content = html_template.render(
#         contact_person=contact_person,
#         company_name=company_name
#     )

#     # Create MIME message
#     msg = MIMEMultipart('alternative')
#     msg['Subject'] = f"Let’s connect, {contact_person}"
#     msg['From'] = EMAIL_ADDRESS
#     msg['To'] = recipient_email
#     msg.attach(MIMEText(html_content, 'html'))

#     try:
#         server.sendmail(EMAIL_ADDRESS, recipient_email, msg.as_string())
#         print(f"Email sent to {recipient_email}")
#     except Exception as e:
#         print(f"Failed to send to {recipient_email}: {e}")

#     emails_sent += 1
#     time.sleep(delay_between_emails)

#     if emails_sent % batch_size == 0:
#         print("Batch sent. Cooling down...")
#         time.sleep(delay_between_batches)

# server.quit()


import smtplib
from jinja2 import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# SMTP credentials
EMAIL_ADDRESS = "hetthakkar158@gmail.com"
EMAIL_PASSWORD = "hoot svip bzgt apil"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# Receiver details
recipient_email = "rudrappatel2004@gmail.com"
contact_person = "Rudra"
company_name = "Rudra Pvt Ltd"

# Load HTML template
with open("email_template.html", "r") as file:
    html_template = Template(file.read())

# Render personalized content
html_content = html_template.render(
    contact_person=contact_person,
    company_name=company_name
)

# Create MIME message
msg = MIMEMultipart('alternative')
msg['Subject'] = f"Let’s connect, {contact_person}"
msg['From'] = EMAIL_ADDRESS
msg['To'] = recipient_email
msg.attach(MIMEText(html_content, 'html'))

# Send the email
try:
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    server.sendmail(EMAIL_ADDRESS, recipient_email, msg.as_string())
    server.quit()
    print(f"Email sent to {recipient_email}")
except Exception as e:
    print(f"Failed to send to {recipient_email}: {e}")
