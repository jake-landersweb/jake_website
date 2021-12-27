from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from . import env


def send_mail(
    recipient, subject, body, is_html=False, sender=env._EMAIL, password=env._PASS,
):
    try:
        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"] = sender
        msg["To"] = recipient

        request = MIMEText(body, "html" if is_html else "plain")

        msg.attach(request)

        with smtplib.SMTP("mailen3.cloudsector.net", port=587) as smtp_obj:
            smtp_obj.ehlo()
            smtp_obj.starttls()
            smtp_obj.ehlo()
            smtp_obj.login(sender, password)

            smtp_obj.sendmail(sender, recipient, msg.as_string())
            smtp_obj.quit()

        return True
    except:
        return False
