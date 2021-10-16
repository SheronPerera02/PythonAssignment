import sys

def user_view():
    file = open('db/session.txt', 'r')
    username = file.read()
    print(username)

def user_login(username):
    file = open('db/session.txt', 'w')
    file.write(username)


class Item:

    def __init__(self, name, price, selling_price):
        self.name = name
        self.price = price
        self.selling_price = selling_price

    def save(self):
        item = {
            'name': self.name,
            'price': self.price,
            'selling_price': self.selling_price,
        }
        print(item)



def item_create(name, price, selling_price):
    item = Item(name, price, selling_price)
    item.save()


def item_all():
    print('All items')

def item_view(id):
    print(id)

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