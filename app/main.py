from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = FastAPI()

class EmailRequest(BaseModel):
    receiver: str
    email_username: str
    email_password: str

@app.post("/send-email/")
async def send_email(email_request: EmailRequest):
    try:
        sender = "your_email@gmail.com"  # Your personalized email address
        receiver = email_request.receiver
        email_username = email_request.email_username
        email_password = email_request.email_password

        # Email content
        subject = "Request for Ledger Submission for Account Reconciliation – Financial Year Ending 23-24"
        body = """
        Dear Creditor Name,

        I hope this email finds you well. As auditors of (Company Name), we are currently in the process of conducting the annual audit for the financial year ending 23-24. As part of this process, we kindly request your cooperation in providing us with your ledger for the aforementioned period.

        The purpose of this request is to facilitate the reconciliation of accounts between (company name) and its creditors. Please provide us with the Ledgers in CSV or Excel format by 15th April 2024. Your prompt attention to this matter would be greatly appreciated.

        If you have any queries or require further clarification, please do not hesitate to contact us. We value your cooperation and assistance in this audit process and look forward to your timely response.

        Thank you for your attention to this matter.

        Thanks & Regards
        """

        # Constructing the email message
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = receiver
        msg.attach(MIMEText(body, 'plain'))

        # Connecting to SMTP server and sending email
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login(email_username, email_password)
        mail.sendmail(sender, receiver, msg.as_string())
        mail.quit()

        return {"message": "Email sent successfully!"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to send email. Error: {str(e)}")
