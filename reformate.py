import email
import smtplib
import imaplib
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart


class Email_messager:
    def __init__(self):
        self.login = "login@gmail.com"
        self.password = "qwerty"
        self.gmail_smtp = "smtp.gmail.com"
        self.subject = "Subject"
        self.gmail_imap = "imap.gmail.com"
        self.recipients = ["vasya@email.com", "petya@email.com"]

    def send_message(self, message):
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(self.recipients)
        msg['Subject'] = self.subject
        msg.attach(MIMEText(message))
        ms = smtplib.SMTP(self.gmail_smtp, 587)
        ms.ehlo()
        ms.starttls()
        ms.ehlo()
        ms.login(self.login, self.password)
        ms.sendmail(self.login, ms, msg.as_string())
        ms.quit()

    def receive_message(self, header=None):
        mail = imaplib.IMAP4_SSL(self.gmail_imap)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()

if __name__ == '__main__':
    Email_messager.send_message('Посылаю сообщение')
    Email_messager.receive_message(header='qwerty')




