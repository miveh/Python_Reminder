import csv

import pandas as pd

from event import event_data, Event


def read_csv_file(filename):
    with open(filename, 'r', newline="") as csvfile:
        csv_reader = csv.reader(csvfile)
        data = list(csv_reader)

    return data


def append_csv_file(filename, row_account):
    with open(filename, 'a', newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(row_account)

    return csv_writer


def write_csv_file(filename, row_account):
    with open(filename, 'w', newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(row_account)

    return csv_writer


def write_rows_csv_file(filename, rows_account):
    with open(filename, 'w', newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(rows_account)


def app_menu(obj):
    while True:
        try:
            selection = int(
                input("\nplease enter item:\n1-add event\n2-change password\n3-edit event\n4-delete event\n5-done an "
                      "event\n6-new category\n7-back\n8-event sharing\nyour selection: "))

            if selection == 1:
                title, link, location, reminder_time, reminder_date, status, category = event_data()
                ev_obj = Event(title, link, location, reminder_time, reminder_date, status, category)
                row_event = [obj.username, ev_obj.title, ev_obj.link, ev_obj.location, ev_obj.reminder_time,
                             ev_obj.reminder_date,
                             ev_obj.status, False, ev_obj.category]
                append_csv_file("event.csv", row_event)

            elif selection == 2:
                new_password = input("new password: ")
                rows_account = read_csv_file("account.csv")
                rows_account = obj.change_password(new_password, rows_account)
                write_rows_csv_file("account.csv", rows_account)

            elif selection == 3:
                rows_event = read_csv_file("event.csv")
                for event in rows_event:
                    if obj.username == event[0]:
                        print(event)
                selected = input("which event? write title: ")
                rows_event = Event.edit(rows_event, selected)
                write_rows_csv_file("event.csv", rows_event)

            elif selection == 4:
                rows_event = read_csv_file("event.csv")
                for event in rows_event:
                    if obj.username == event[0]:
                        print(event)
                the_event = input("title event for remove it: ")
                new_rows_event = Event.remove(rows_event, obj, the_event)
                write_rows_csv_file("event.csv", new_rows_event)
                print("\nevent remove successfully !!")

            elif selection == 5:
                rows_event = read_csv_file("event.csv")
                for event in rows_event:
                    if event[0] == obj.username:
                        print(event)
                the_event = input("title event for done it: ")
                new_rows_event = Event.done(rows_event, obj, the_event)
                write_rows_csv_file("event.csv", new_rows_event)
                print("\nevent done successfully !!")

            elif selection == 6:
                category_list = read_csv_file("category.csv")
                print([category[0] for category in category_list])
                selected = input("enter new category: ")
                f = open("category.csv", 'a')
                f.write(selected)
                f.write('\n')
                f.close()
                print("new category added!!")
            elif selection == 7:
                break

            elif selection == 8:
                try:
                    selection = int(input("\n1-new Post\n2-received\nenter 1 or 2 : "))
                    if selection == 1:
                        rows_event = read_csv_file("event.csv")
                        for event in rows_event:
                            if event[0] == obj.username:
                                print(event)
                        the_event = input("write title for sharing: ")
                        for event in rows_event:
                            if event[1] == the_event:
                                pandas_reader = pd.read_csv("account.csv")
                                lst_username = list(pandas_reader['username'])
                                print("\nusers:\n", lst_username)
                                the_user = input("\nselect a user for sharing...\n")
                                row_sharing = [obj.username, the_user, event[1], event[2], event[3], event[4], event[5], event[6], event[7], event[8], "waiting"]
                                append_csv_file("requests.csv", row_sharing)

                    elif selection == 2:
                        rows_request = read_csv_file("requests.csv")
                        for request in rows_request:
                            if request[1] == obj.username:
                                print(request)
                        selected = input("write title for accept or reject request: ")
                        selected_1 = int(input("\n1-accept\n2-reject\n: "))
                        for request in rows_request:
                            if request[2] == selected:
                                if selected_1 == 1:
                                    request[10] = "accept"
                                    row_event = [obj.username, request[2], request[3], request[4],
                                                 request[5], request[6], request[7], False, request[9]]
                                    append_csv_file("event.csv", row_event)

                                elif selected_1 == 2:
                                    request[10] = "reject"
                        write_rows_csv_file("requests.csv", rows_request)
                    else:
                        raise Exception("value error!!")
                except Exception as e:
                    print(e)
            else:
                raise Exception("invalid option!! try again")
        except Exception as e:
            print(e)
