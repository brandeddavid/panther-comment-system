import datetime

def login(username, password):

    for user in users:

        if username in user.values():

            if user['password'] == password:

                if user['userType'] == 1:

                    admin()

                elif user['userType'] == 2:

                    moderator()

                else:

                    normal()

            else:

                return 'Passwords Do not Match'
        else:

            return 'User Does Not Exist'

def main():

    while True:

        username = str(input("Enter Username: "))
        password = str(input("Enter Password: "))

        login(username=username, password=password)


if __name__ == '__main__':

    main()