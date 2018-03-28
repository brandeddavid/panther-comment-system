import datetime
from time import gmtime, strftime

users = [
    {
        "id": 1, 'username': 'admin', 'password': 'admin', 'userType': 1, "lastLogin": None
    },
    {
        "id": 2, 'username': 'sam', 'password': 'sam', 'userType': 3, "lastLogin": None
    },
    {
        "id": 3, 'username': 'brian', 'password': 'brian', 'usetType': 2, "lastLogin": None
    },
    {
        "id": 4, 'username': 'david', 'password': 'david', 'usetType': 3, "lastLogin": None
    },
]


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
