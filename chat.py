import datetime

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
