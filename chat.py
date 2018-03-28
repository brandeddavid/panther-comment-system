import datetime
from time import gmtime, strftime

# Comments list
comments = [
    {"id":1, "commentMessage":"First message", "author":"Brian", "timeStamp":23-5-2018, "isParent": True},
    {"id":2, "commentMessage":"Second message", "author":"David", "timeStamp":21-7-2018, "isParent": False, "parent":1}
]

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

def getUserName(user):
    for x in users:
        print(x)
        if x == user:
            return user.get("username")
    return 0


def moderator(usr):
    user = getUserName(usr)
    print("What do you wish to do?")
    print("Enter 1 to add comment")
    print("Enter 2 to edit comment")
    print("Enter 3 to delete comment")

    action = input('> ')

    if action == 1 or action == '1':
        comment = input("Please enter you comment: ")
        addCommment(user, comment)
        print(comments)
        pass

    elif action == 2 or action == '2':
        commentId = input("Please enter id of comment to edit: ")
        comment = input("Please enter new comment: ")
        editComment(commentId, comment)
        print(comments)
        pass

    elif action == 3 or action == '3':
        pass
    else:
        print("You entered an invalid option")
        moderator()


def addCommment(user, comment):
    index = len(comments) + 1
    comments.append([{"id": index, "comment": comment, "author": user, "timeStamp": datetime.datetime.now(),
                      "isParent": True, "parent": None}])
    pass

def editComment(commentId, newComment):
    comment = [comment for comment in comments if comment['id'] == commentId]
    comment[0]['comment'] = newComment
    pass

moderator({'id': 1, 'username': 'admin', 'password': 'admin', 'userType': 1, 'lastLogin': None})

# Admin function
def admin(user):
    print('What do you want to do? \n')
    print('Enter 1 for Edit comment\n')
    print('Enter 2 for Delete comment\n')
    
    prompt = input('> ')

    if prompt == str(1):
        print('Here is a list of all the comments: ')
        print(*comments, sep='\n')
        print('Select comment to edit: ')

    elif prompt == str(2):
        pass

    else:
        pass 

def normal(user):

    print('What would like to do:\n')
    print('Enter 1 for add comment\n')
    print('Enter 2 for edit comment\n')
    print('Enter 3 to reply to comment\n')

    prompt = input('> ')

    if prompt == str(1):

        prompt = input('Enter Comment: ')

        addComment(user['username'], prompt)

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

