import csv

import jdatetime
from time import sleep
import threading

import menu


class Event:
    """
        Define a personal event
    """

    def __init__(self, title, link, location, reminder_time, reminder_date, status, category):
        self.title = title
        self.link = link
        self.location = location
        self.reminder_time = reminder_time
        self.reminder_date = reminder_date
        self.status = status
        self.done = False
        self.category = category

    def reminder(self, status):
        """
            remembering events manage here basic status
        """

        def printit():
            if today <= self.reminder_date:
                if now <= self.reminder_time:
                    threading.Timer(5.0, printit).start()
                    print("event warning!!")

        if self.status == 1:
            now = jdatetime.datetime.now().time()
            today = jdatetime.datetime.now().date()
            printit()
        elif self.status == 2:
            now = jdatetime.datetime.now().time()
            today = jdatetime.datetime.now().date()
            if today == self.reminder_date:
                if now == self.reminder_time:
                    print("\nRemid time of your personal event!!\n")
                else:
                    pass
        elif self.status == 3:
            now = jdatetime.datetime.now().time()
            today = jdatetime.datetime.now().date()
            if today <= self.reminder_date:
                if now <= self.reminder_time:
                    if now == jdatetime.time(23, 59, 59):
                        print("\nRemind time of your personal event!!\n")
        elif self.status == 4:
            now = jdatetime.datetime.now().time()
            today = jdatetime.datetime.now().date()
            if today <= self.reminder_date:
                if now <= self.reminder_time:
                    if jdatetime.datetime.now().date().strftime('%A') == "Friday":
                        print("\nRemind time of your personal event!!\n")

    @staticmethod
    def completion(csv_file_name):
        """
            Apply changes to the event upon completion
            Convert attribute done status from true to false
        """
        filepath = csv_file_name
        with open(filepath, 'r', newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            list_of_list = list(csv_reader)

        for event in list_of_list:
            print(event[0])

        the_event = input("\nEND AN EVENT\nenter title of event: ")
        with open(filepath, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)

            for event in list_of_list:

                if event[0] == the_event:

                    event[6] = "True"
                    print(event)
                    csv_writer.writerow(event)

                else:

                    csv_writer.writerow(event)

    @staticmethod
    def category():
        """
            Define categories for events
        """
        filepath = "category.csv"
        while True:
            the_category = input("enter categry or \'0\' for exit: ")
            if the_category == '0':
                break

            else:
                with open(filepath, 'a', newline='') as csvfile:
                    csvfile.write(the_category)
                    csvfile.write(",")
                    csvfile.write("\n")
                    print("\nnew category added successfully!!\n")


def calendar_view():
    """
        View events on a calendar
    """
    pass
