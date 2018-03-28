import datetime

# Comments list
comments = [
    {"id":1, "commentMessage":"First message", "author":"Brian", "timeStamp":23-5-2018, "isParent": True},
    {"id":2, "commentMessage":"Second message", "author":"David", "timeStamp":21-7-2018, "isParent": False, "parent":1}
]


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