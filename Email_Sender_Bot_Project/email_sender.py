import smtplib
import pandas as pd
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

YOUR_EMAIL = "your_email@gmail.com"
YOUR_APP_PASSWORD = "your_app_password"

RECIPIENTS_CSV = "recipients.csv"
ATTACHMENT_FILE = "sample.pdf"

SUBJECT = "Automated Email - Syntecxhub Internship"
MESSAGE_BODY = """Hello {name},

This is an automated message sent using Python.
Your internship email bot project is working successfully!

Thank you,
Syntecxhub Internship Team
"""

def send_email(to_email, name, attachment_path=None, retry=3):
    for attempt in range(retry):
        try:
            msg = MIMEMultipart()
            msg['From'] = YOUR_EMAIL
            msg['To'] = to_email
            msg['Subject'] = SUBJECT

            body = MESSAGE_BODY.format(name=name)
            msg.attach(MIMEText(body, 'plain'))

            if attachment_path:
                try:
                    attachment = open(attachment_path, "rb")
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', f'attachment; filename="{attachment_path}"')
                    msg.attach(part)
                except:
                    print(f"Attachment not found: {attachment_path}")

            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            server.starttls()
            server.login(YOUR_EMAIL, YOUR_APP_PASSWORD)
            server.send_message(msg)
            server.quit()

            print(f"SUCCESS: Email sent to {name} <{to_email}>")
            return True
        except Exception as e:
            print(f"ERROR Attempt {attempt+1} failed for {to_email}: {e}")
            time.sleep(2)
    print(f"FAILED: Could not send email to {to_email}")
    return False

def main():
    try:
        data = pd.read_csv(RECIPIENTS_CSV)
    except:
        print("ERROR reading recipients.csv")
        return

    for _, row in data.iterrows():
        send_email(row['email'], row['name'], ATTACHMENT_FILE)

if __name__ == "__main__":
    main()
