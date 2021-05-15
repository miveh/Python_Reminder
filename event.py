import threading

import jdatetime

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

    @staticmethod
    def edit(rows_event, selected):
        try:
            for event in rows_event:
                if event[1] == selected:
                    event[1], event[2], event[3], event[4], event[5], event[6], event[8] = event_data()
                    event[7] = False
                    break
            else:
                raise Exception("not find")
        except Exception as e:
            print(e)

        return rows_event

    @staticmethod
    def remove(rows_event, obj, the_event):
        new_rows_event = []
        try:
            for event in rows_event:
                if obj.username == event[0] and event[1] == the_event:
                    pass
                else:
                    new_rows_event.append(event)
        except:
            print("error!!")

        return new_rows_event

    @staticmethod
    def done(rows_event, obj, the_event):
        try:
            for event in rows_event:
                if obj.username == event[0] and event[1] == the_event:
                    event[7] = True
                    break
            else:
                raise Exception("not find event!!")
        except Exception as e:
            print(e)

        return rows_event

    def reminder(self):
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
                    print("\nRemind time of your personal event with status \'2\'!!\n")
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

    category_lst = menu.read_csv_file("category.csv")
    print(category_lst)
    category = input("\nwrite a category from category-list: \n")

    return title, link, location, reminder_time, reminder_date, status, category
