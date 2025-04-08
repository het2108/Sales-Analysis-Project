import smtplib
from jinja2 import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


EMAIL_ADDRESS = "hetthakkar158@gmail.com"
EMAIL_PASSWORD = "hoot svip bzgt apil"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587


recipient_email = "22002170110040@ljku.edu.in"
contact_person = "Rudra"
company_name = "Rudra Pvt Ltd"


with open("email_template.html", "r") as file:
    html_template = Template(file.read())

#To initialize all variables in the template
html_content = html_template.render(
    contact_person=contact_person,
    company_name=company_name,
    lead_id=recipient_email
)

# Create's MIME message
msg = MIMEMultipart('alternative')
msg['Subject'] = f"Quick question for {contact_person}"
msg['From'] = EMAIL_ADDRESS
msg['To'] = recipient_email
msg.attach(MIMEText(html_content, 'html'))

#Sending the mail
try:
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    server.sendmail(EMAIL_ADDRESS, recipient_email, msg.as_string())
    server.quit()
    print(f"Email sent to {recipient_email}")
except Exception as e:
    print(f"Failed to send to {recipient_email}: {e}")
