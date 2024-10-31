# notification.py
import smtplib
from email.mime.text import MIMEText

class Notification:
    def __init__(self):
        self.limit = 0

    def set_limit(self, limit):
        self.limit = limit

    def send_notification(self, expense):
        if expense[3] > self.limit:
            msg = MIMEText("Expense exceeds limit: {}".format(expense[3]))
            msg["Subject"] = "Expense Notification"
            msg["From"] = "digitalbhem_project@gmail.com"
            msg["To"] = "prudvivadhi111@gmail.com"
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login("digitalbhem_project@gmail.com", "passowrd")
            server.sendmail("digitalbhem_project@gmail.com", "prudvivadhi111@gmail.com", msg.as_string())
            server.quit()

