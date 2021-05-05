import csv
import jdatetime
from event import Event
from user import User


def event_data():
    title = input("\nDATA EVENT\nenter description: ")
    link = input("enter link: ")
    location = input("enter location: ")
    input_time = input("enter event time in format (HH:MM): ")
    input_date = input("enter event date as jalaly:(yy/mm/dd): ")

    year, month, day = map(int, input_date.split('/'))
    reminder_date = jdatetime.date(year, month, day)
    hour, minutes = map(int, input_time.split(':'))
    reminder_time = jdatetime.time(hour, minutes, second=00)

    status = int(input("\nSelect the status of this event:\n\n              Urgent      not "
                       "Urgent\n    important   1           3\nnot important   2          "
                       " 4\n"))

    f = open("category.csv", 'r')
    print(f.read())
    category = input("enter a category from category-list")

    return title, link, location, reminder_time, reminder_date, status, category


def edit(csv_file_name):
    filename = csv_file_name

    with open(filename, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        list_of_list = list(csv_reader)

    for event in list_of_list:
        print(event[0])

    the_event = input("enter title of event: ")

    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)

        for event in list_of_list:

            if the_event == event[0]:

                title, link, location, reminder_time, reminder_date, status, category = event_data()
                ev_obj = Event(title, link, location, reminder_time, reminder_date, status, category)
                row_event = [ev_obj.title, ev_obj.link, ev_obj.location, ev_obj.reminder_time,
                             ev_obj.reminder_date, ev_obj.status, False, ev_obj.category]

                print("\nevent update successfully!!\n")
                csv_writer.writerow(row_event)

            else:
                csv_writer.writerow(event)


def remove(csv_file_name):
    """
        Remove an event with this method
    """
    filename = csv_file_name

    with open(filename, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        list_of_list = list(csv_reader)

    for event in list_of_list:
        print(event[0])

    the_event = input("title event for remove it: ")

    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)

        for event in list_of_list:

            if the_event == event[0]:

                pass

            else:

                csv_writer.writerow(event)

    print("\nevent remove successfully!!\n")


def app_menu(username):
    while True:

        selection = int(
            input("\nplease enter item:\n1-add event\n2-change password\n3-edit event\n4-delete event\n5-end an "
                  "event\n6-new category\n7-back\nyour selection: "))

        if selection == 1:

            title, link, location, reminder_time, reminder_date, status, category = event_data()

            ev_obj = Event(title, link, location, reminder_time, reminder_date, status, category)

            row_event = [ev_obj.title, ev_obj.link, ev_obj.location, ev_obj.reminder_time, ev_obj.reminder_date,
                         ev_obj.status, False, ev_obj.category]

            with open("event.csv", 'a', newline='') as csv_event:
                csv_writer = csv.writer(csv_event)
                csv_writer.writerow(row_event)

        elif selection == 2:

            User.change_password(username)

        elif selection == 3:

            edit("event.csv")

        elif selection == 4:
            remove("event.csv")

        elif selection == 5:

            Event.completion("event.csv")

        elif selection == 6:

            Event.category()

        elif selection == 7:

            break
