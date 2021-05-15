from menu import append_csv_file, read_csv_file, app_menu
from user import User, user_data
import pandas as pd


while True:

    try:
        print('please enter one item\n1-login\n2-sign up\n3-exit')
        selection_item = int(input('your selection: '))

        if selection_item == 1:

            rows_account = read_csv_file("account.csv")
            username, password = user_data()
            obj_user = User(username, password)
            obj_user.login(rows_account)
            app_menu(obj_user)

        elif selection_item == 2:

            try:
                pandas_reader = pd.read_csv("account.csv")
                lst_username = list(pandas_reader['username'])
                if not lst_username:
                    raise Exception("empty file!")
            except:
                lst_username = ['00']  # kalak rashti

            username, password = user_data()
            obj_user = User(username, password)
            row_account = obj_user.register(lst_username)
            append_csv_file("account.csv", row_account)

        elif selection_item == 3:

            exit()

        else:
            raise Exception("Invalid option!! try again:")

    except Exception as e:
        print(e)
