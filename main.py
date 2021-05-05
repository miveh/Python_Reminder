from menu import app_menu
from user import User

while True:

    print('please enter one item\n1-login\n2-sign up\n3-exit')
    selection_item = int(input('your selection: '))


    if selection_item == 1:
        username_ = User.login()
        app_menu(username_)
    elif selection_item == 2:
        User.register()
    elif selection_item == 3:
        exit()
    else:
        print('\ninvalid input, try again\n')