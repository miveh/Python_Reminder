import hashlib

from menu import write_csv_file, read_csv_file


class User:

    def __init__(self, username, password):

        self.username = username
        self.password = password

    def register(self, lst_username):

        while True:
            try:
                if self.username in lst_username:
                    raise Exception("username taken!! try again:")
                else:
                    break
            except Exception as e:
                print(e)
                self.username = input("username: ")

        hash_password = hashlib.sha256(self.password.encode('utf8')).hexdigest()
        row_account = [self.username, hash_password]

        return row_account

    def login(self, rows_account):
        flag = 0
        while flag == 0:
            try:
                for row in rows_account:
                    if self.username == row[0]:
                        while True:
                            try:
                                hash_password = hashlib.sha256(self.password.encode('utf8')).hexdigest()
                                if hash_password == row[1]:
                                    print("\nyour login success!!\n")
                                    break  # while
                                else:
                                    raise Exception("wrong password!! try again:")
                            except Exception as e:
                                print(e)
                                self.password = input("password: ")
                        flag = 1
                        break
                else:
                    raise Exception("invalid username!! try again:")
            except Exception as e:
                print(e)
                self.username = input("username: ")

    def change_password(self, new_password, rows_account):
        new_hash_password = hashlib.sha256(new_password.encode('utf8')).hexdigest()
        try:
            for row in rows_account:
                if row[0] == self.username:
                    row[1] = new_hash_password
                    print("\npassword change successfully!!\n")
                    break
            else:
                raise Exception("user not found!!")

        except Exception as e:
            print(e)

        return rows_account




def user_data():
    username = input("username: ")
    password = input("password: ")

    return username, password
