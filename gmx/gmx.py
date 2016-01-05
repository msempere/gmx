import imaplib

from mailbox import Mailbox
from utf import encode as encode_utf7, decode as decode_utf7
from exceptions import *

class Gmx():
    GMX_IMAP_HOST = 'imap.gmx.com'
    GMX_IMAP_PORT = 993

    def __init__(self):
        self.username = None
        self.password = None
        self.access_token = None

        self.imap = None
        self.smtp = None
        self.logged_in = False
        self.mailboxes = {}
        self.current_mailbox = None

    def connect(self, raise_errors=True):
        self.imap = imaplib.IMAP4_SSL(self.GMX_IMAP_HOST, self.GMX_IMAP_PORT)
        return self.imap


    def fetch_mailboxes(self):
        response, mailbox_list = self.imap.list()
        if response == 'OK':
            for mailbox in mailbox_list:
                mailbox_name = mailbox.split('"/"')[-1].replace('"', '').strip()
                mailbox = Mailbox(self)
                mailbox.external_name = mailbox_name
                self.mailboxes[mailbox_name] = mailbox

    def use_mailbox(self, mailbox):
        if mailbox:
            self.imap.select(mailbox)
        self.current_mailbox = mailbox

    def mailbox(self, mailbox_name):
        if mailbox_name not in self.mailboxes:
            mailbox_name = encode_utf7(mailbox_name)
            mailbox = self.mailboxes.get(mailbox_name)

        if mailbox and not self.current_mailbox == mailbox_name:
            self.use_mailbox(mailbox_name)

        return mailbox

    def login(self, username, password):
        self.username = username
        self.password = password

        if not self.imap:
            self.connect()

        try:
            imap_login = self.imap.login(self.username, self.password)
            self.logged_in = (imap_login and imap_login[0] == 'OK')
            if self.logged_in:
                self.fetch_mailboxes()
        except imaplib.IMAP4.error:
            raise AuthenticationError

        return self.logged_in

    def logout(self):
        self.imap.logout()
        self.logged_in = False

    def find(self, mailbox_name="[Gmail]/All Mail", **kwargs):
        box = self.mailbox(mailbox_name)
        return box.mail(**kwargs)

    def inbox(self):
        return self.mailbox("INBOX")

    def mail_domain(self):
        return self.username.split('@')[-1]
