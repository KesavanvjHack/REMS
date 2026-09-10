import imaplib
import email
import sys

try:
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login('g.kesavaperumalvnr@gmail.com', 'ygzmvnvdiaydhvvp')
    
    def check_folder(folder_name):
        mail.select(folder_name)
        status, messages = mail.search(None, 'ALL')
        if status == 'OK':
            msg_ids = messages[0].split()
            print(f'Found {len(msg_ids)} total emails in {folder_name}')
            for msg_id in msg_ids[-5:]:
                res, msg_data = mail.fetch(msg_id, '(BODY[HEADER.FIELDS (SUBJECT DATE)])')
                for response_part in msg_data:
                    if isinstance(response_part, tuple):
                        msg = email.message_from_bytes(response_part[1])
                        print(f'   -> Date: {msg["Date"]}, Subject: {msg["Subject"]}')
        else:
            print(f'Failed to search {folder_name}')

    check_folder('INBOX')
    check_folder('"[Gmail]/Spam"')
    
    mail.logout()
except Exception as e:
    print('Error:', e)
