import datetime


def normal(user):

    print('What would like to do:\n')
    print('Enter 1 for add comment\n')
    print('Enter 2 for edit comment\n')
    print('Enter 3 to reply to comment\n')

    prompt = input('> ')

    if prompt == str(1):
        prompt = input('Enter Comment: ')
        comment = {}
        comment['id'] = 123
        comment['commentMessage'] = prompt
        comment['author'] = user['username']
        comment['timeStamp'] = datetime.datetime.now()
        comment['isParent'] = True
        comment['parent'] = None

        comments.append(comment)

    elif prompt == str(2):

        print('Here is a list of all your comments: ')

    else:

        pass


def login(username, password):

    for user in users:

        if username in user.values():

            if user['password'] == password:

                if user['userType'] == 1:

                    admin(user)

                elif user['userType'] == 2:

                    moderator(user)

                else:

                    normal(user)

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