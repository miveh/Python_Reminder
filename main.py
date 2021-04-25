import datetime
import csv

class Account:
    '''
        Define a user
    '''
    def __init__(self, username, password, mail):
        self.username = username
        self.password = password
        self.mail = mail

    def __str__(self):
        return f'new account created as username: {self.username},pass: {self.password},mail: {self.mail}'

class Event:
    '''
        Define a personal event
    '''
    def __init__(self, title, link, location, reminder_hour, reminder_date ):
        self.title = title
        self.link = link
        self.location = location
        self.reminder_hour = reminder_hour
        self.reminder_date = reminder_date
        self.done = False
    
    def reminder(self):
        '''
            rememebering events manage here
        '''
        pass

    def importance(self):
        '''
            Record the importance and urgency of
            the event based on the Eisenhower matrix
        '''
        pass
        #return importance

    def add(self):
        '''
            Add an event with this method
        '''
        pass

    def edit(self):
        '''
            Edit an event with this method
        '''
        pass

    def delay(self):
        '''
            To postpone the event
        '''
        pass

    def completion(self):
        '''
            Apply changes to the event upon completion
            Convert attribute done status from true to false
        '''
        pass

    def category(self):
        '''
            Define categories for events
        '''
        pass


def calendar_view():
    '''
        View events on a calendar
    '''
    pass


#Events submitted by other users to this user awaiting rejection or acceptance
Invited_events = []#[[username ,Acceptance status of an event]] 

#This is the place to create a method or ... to record all the information in file

#and logging ...

#Body and menu 'without' Error handeling in this phaz
while True:
    selection = int(input('for create an account please enter 1: \ndo you have an account?enter 2: '))
    if selection == 1:
        username = input('for create account, please enter name: ')
        password = input('Enter a password that contains 5 characters and a number: ')
        mail = input('enter a valid mail(email/gmail): ')
        account = Account(username, password, mail)
        with open('account_file.csv', mode='w') as account_file:
            account_writer = csv.writer(account_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            account_writer.writerow([account.username, account.password, account.mail])
        print(account.__str__())
        

    elif selection == 2:
        username = input('please enter username: ')
        password = input('enter password for login: ')
        with open('account_file.csv', mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:#warning! i shoud write a code for delete end-breaking in each line
                if username == row[0]:
                    if password == row[1]:
                        #show menu
                        print(row)
                        print('blahblah')
                    else:
                        pass        
                else:
                    print('not blahblah')
                    #Error handeling
        

    else:
        print("Invalid input, please try again")
        