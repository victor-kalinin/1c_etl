import smtplib
from email.message import EmailMessage
from logging.handlers import BufferingHandler

from app.config.email_settings import EmailSettings


class BufferingSMTPHandler(BufferingHandler, EmailSettings):
    def __init__(self, capacity):
        super().__init__(capacity)
        self.PORT = smtplib.SMTP_PORT if self.PORT is None else self.PORT
        self.msg = EmailMessage()

    def flush(self):
        if len(self.buffer) > 0:
            log_records = [self.format(record) for record in self.buffer]
            self.msg['Subject'] = self.SUBJECT
            self.msg['From'] = self.FROM
            self.msg['To'] = ', '.join(self.TO)
            self.msg.set_content('\r\n'.join(log_records))

            with smtplib.SMTP(self.MAILHOST, self.PORT) as smtp:
                smtp.send_message(self.msg)
            super().flush()
