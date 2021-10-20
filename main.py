from item import *


# def __init__():
#     os.makedirs(name)


def user_view():
    file = open('db/session.txt', 'r')
    username = file.read()
    print(username)

def user_login(username):
    file = open('db/session.txt', 'w')
    file.write(username)


if __name__ == '__main__':
    arguments = sys.argv[1:]

    section = arguments[0]
    command = arguments[1]
    params = arguments[2:]

    if section == 'user':
        if command == 'login':
            user_login(*params)
        elif command == 'view':
            user_view()
    elif section == 'item':
        if command == 'create':
            item_create(*params)
        elif command == 'all':
            item_all()
        elif command == 'view':
            item_view(*params)
        elif command == 'search':
            item_search(*params)

