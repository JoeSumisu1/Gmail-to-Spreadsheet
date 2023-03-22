from gmail_connect import retrieve_gmail
import re

def process():
    '''
    description:
        takes the list from retrieve_gmail() and extracts the strings which immediately follow the following keywords:
    ('account name:', 'broker:', 'business unit:', 'due date:', 'underwriter:', 'sender:'). Returns
    a list of lists in an organized format which allows for csv creation or editing of google sheets

    returns:
        a list of lists containing relevant data
    '''

    # data to be extracted
    headers = ['account name:', 'broker:', 'business unit:', 'due date:', 'underwriter:', 'sender:']

    split_messages = []

    #extracts a list of relevant data from the email content. This list is then added to split_messages for further processing
    split_messages.append(headers)
    for message in retrieve_gmail():
        split_message = []
        for test_head in headers:
            part_mess = message.split(test_head)[1]
            new = re.split('account name:|broker:|business unit:|due date:|underwriter:|sender:|\n', part_mess)[0].strip()
            split_message.append(new)
        split_messages.append(split_message)

    return split_messages



