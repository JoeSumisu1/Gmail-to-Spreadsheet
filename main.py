import gspread
import process_messages
import pandas as pd

def add_spreadsheet(file_name="file name here", sheet_name='sheet tab name'):
    '''
    description:
        adds the extracted data to a specified google sheet. Note all cells in google sheet are cleared each time
        code is executed

    params:
        file_name: name of google sheet to edit
        sheet_name: name of google sheet tab to edit
    '''
    #google sheets edit
    processed_list = process_messages.process()
    sa = gspread.service_account(filename='credentials.json')
    sh = sa.open(file_name)
    wks = sh.worksheet(sheet_name)

    wks.clear()

    for mesid, message in enumerate(processed_list):
        for iditem, item in enumerate(message):
            alphabet = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
            try:
                cell = alphabet[iditem]+str(mesid+1)
                wks.update(f'{cell}', item)
            except:
                pass


def create_csv(path='account_details.csv'):
    '''
    description:
        creates a csv of extracted data in specified path. Creates new csv 'account_details.csv' in current working
        directory by default if no path or file name specified

    params:
        path: file path to save csv
    '''
    df = pd.DataFrame(process_messages.process())
    df.to_csv(path, header=False)


add_spreadsheet()