import pandas as pd
import hashlib
import csv
# import shutil
# from tempfile import NamedTemporaryFile


class User:

    def __init__(self, username, password):

        self.username = username
        self.password = password

    @staticmethod
    def login():

        flag = 0
        file_path = "account.csv"

        while flag == 0:

            with open(file_path, 'r') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                username = input("enter username: ")

                for row in csv_reader:

                    if username == row[0]:

                        while True:

                            password = input("Enter password: ")
                            hash_password = hashlib.sha256(password.encode('utf8')).hexdigest()

                            if hash_password == row[1]:

                                print("\nyour login success!!\n")
                                break  # while

                            else:

                                print("\nwrong password!\n")

                        flag = 1
                        break  # for

                else:

                    print(f"\n\'{username}\' not a user! tray again\n")

        return username

    @staticmethod
    def register():

        file_path = "account.csv"
        df_account = pd.read_csv(file_path)
        lst_username = list(df_account['username'])

        while True:

            username = input('enter username: ')

            if username in lst_username:

                print("The user has already been created. Enter a valid name\n")

            else:

                break

        password = input('enter password: ')
        hash_password = hashlib.sha256(password.encode('utf8')).hexdigest()
        obj_user = User(username, hash_password)
        row_account = [[obj_user.username, obj_user.password]]

        with open(file_path, 'a', newline='') as csv_account:
            csv_writer = csv.writer(csv_account)
            # writing the data row
            csv_writer.writerows(row_account)

        print("\naccount create successfully\n")

    @staticmethod
    def change_password(username):

        filename = "account.csv"
        # header = ["username", "password"]
        new_password = input(f"new password for \'{username}\': ")
        new_hash_password = hashlib.sha256(new_password.encode('utf8')).hexdigest()

        with open(filename, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            list_of_list = list(csv_reader)

        with open(filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)

            for row in list_of_list:

                if row[0] == username:

                    row[1] = new_hash_password
                    print(row)
                    csv_writer.writerow(row)

                else:

                    csv_writer.writerow(row)
