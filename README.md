# Gmail-to-Spreadsheet
## OVERVIEW
* In my previous role as a catastrophe modeler, the modeling team recieved analysis requests through email to a shared inbox. Each email contained information on the account to be modeled, such as the name of the broker, account name, business unit, due date and other relavent data. In order to track all the modeling requests, I had the repetitive task of manually transferring this data from each email to a spreadsheet. I thought this would be a great process to automate due to its repetitive nature so I wrote a python script to perform this task.

## FILES
* gmail_connect.py: connects to gmail's IMAP server and returns a list of messages that fall under specified header
* process_messages.py: takes the list from retrieve_gmail() and extracts the strings which immediately follow the following labels: ('account name:', 'broker:', 'business unit:', 'due date:', 'underwriter:', 'sender:'). 
* main.py: contains 2 functions, add_spreadsheet & create_csv. Calling the spreadsheet function will edit a specified google sheet. Calling the create_csv function will create a csv file to the specified path 


![email](https://user-images.githubusercontent.com/128116246/229334303-9379bff7-0499-4517-8ba9-e5770abb715d.png)
<img width="452" alt="Screen Shot 2023-04-02 at 1 49 11 AM" src="https://user-images.githubusercontent.com/128116246/229334475-434d931c-c774-41d0-97e3-6b4220e52b99.png">



