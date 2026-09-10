import smtplib
from email.mime.text import MIMEText

def test_email():
    sender = "g.kesavaperumalvnr@gmail.com"
    password = "ygzmvnvdiaydhvvp"
    recipient = "g.kesavaperumalvnr@gmail.com"
    
    msg = MIMEText("This is a test email from your Django backend configuration to verify that the App Password is correct.")
    msg['Subject'] = "Test Email Verification"
    msg['From'] = sender
    msg['To'] = recipient

    try:
        print("Connecting to Gmail SMTP server...")
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.set_debuglevel(1)
        server.starttls()
        print("Logging in...")
        server.login(sender, password)
        print("Sending email...")
        server.send_message(msg)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    test_email()
