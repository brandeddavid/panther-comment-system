import datetime

# Comments list
comments = [
    {"id":1, "commentMessage":"First message", "author":"Brian", "timeStamp":23-5-2018, "isParent": True},
    {"id":1, "commentMessage":"Second message", "author":"David", "timeStamp":21-7-2018, "isParent": False}
]

# Admin function
def admin():
    print('What do you want to do? \n')
    print('Enter 1 for Edit comment\n')
    print('Enter 2 for Delete comment\n')

    prompt = input('> ')

    if prompt == str(1):
        pass

    elif prompt == str(2):
        pass

    else:
        pass