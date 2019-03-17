import imaplib
from configuration.config import Config
import time

config = Config()


def get_login_passcode(sleep):
    # This method grabs latest email, retrieves SMS 6 digit Passcode that was
    # texted to the phone mumber associated with user account
    imap_url = 'imap.gmail.com'
    user_info = config.credentials
    time.sleep(sleep)
    mail = imaplib.IMAP4_SSL(imap_url)
    mail.login(user=user_info['gmail_user']['email'], password=user_info['gmail_user']['password'])
    mail.list()
    mail.select("inbox")

    result, data = mail.search(None, "ALL")

    ids = data[0]
    id_list = ids.split()
    latest_email_id = id_list[-1]

    results, data = mail.fetch(latest_email_id, "(RFC822)")

    raw_email = str(data[0][1])
    print(raw_email)
    if "is your verification code for Endpoint" in raw_email:
        passcode_index = raw_email.find("is your verification code for Endpoint")
        sms_passcode = raw_email[passcode_index - 7:passcode_index]
        print(sms_passcode)
        return str(sms_passcode)
    else:
        return False
