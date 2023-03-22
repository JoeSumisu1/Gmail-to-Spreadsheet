import imaplib
import email
from email.header import decode_header

def retrieve_gmail(subject='header_here', username = 'gmail address here', password = 'gmail password'):
    '''
    description:
        Connects to gmail's IMAP server and returns a list of messages that fall under specified header

    params:
        subject: header of emails to read
        username: gmail address
        password: gmail password

    returns:
        a list of email body as strings
    '''

    # IMAP server settings for Gmail
    imap_host = 'imap.gmail.com'
    imap_port = 993

    # Connect to Gmail's IMAP server
    imap = imaplib.IMAP4_SSL(imap_host, imap_port)

    # Login to your account
    imap.login(username, password)

    # Select the mailbox you want to read from
    imap.select('INBOX')

    # Search for emails in the mailbox with the specified subject line
    typ, data = imap.search(None, f'SUBJECT "{subject}"')

    #list of messages
    messages = []

    # Iterate through the list of email IDs returned by the search
    for num in data[0].split():
        # Fetch the email using its ID
        typ, data = imap.fetch(num, '(RFC822)')
        raw_email = data[0][1]

        # Convert the raw email to a Python object
        email_message = email.message_from_bytes(raw_email)
        sender_name, _ = decode_header(email.message_from_bytes(data[0][1])['From'])[0]

        # Extract the message body
        for part in email_message.walk():
            if part.get_content_type() == 'text/plain':
                message_body = part.get_payload(decode=True).decode('utf-8')
                break

        # add the sender name and body of the email to messages list
        messages.append(f'{message_body.lower()} sender: {sender_name}')
    return messages

