from item import *
from cart import *
from auth import *

if __name__ == '__main__':
    arguments = sys.argv[1:]

    section = arguments[0]
    command = arguments[1]
    params = arguments[2:]

    if section == 'user':
        if command == 'signup':
            user_signup(*params)
        elif command == 'signin':
            user_signin(*params)
        elif command == 'signout':
            user_signout()
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
    elif section == 'cart':
        if command == 'add':
            cart_add(*params)
        elif command == 'remove':
            cart_remove(*params)

