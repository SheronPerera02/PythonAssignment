import sys
import json
import os

__items_folder__ = 'db/items'
__item_id_path__ = 'db/item_id'


class Item:

    def __init__(self, name, price, selling_price):
        self.name = name
        self.price = price
        self.selling_price = selling_price

    def save(self):
        data = {
            'name': self.name,
            'price': self.price,
            'selling_price': self.selling_price,
        }

        readItemId = open(__item_id_path__, 'r')
        id = readItemId.read()
        newId  = 0

        if id == '':
            writeItemsFolder = open(__items_folder__+'/1.json', 'w')
            json.dump(data, writeItemsFolder)
            newId = 2
        else:
            writeItemsFolder = open(__items_folder__+'/'+str(id)+'.json', 'w')
            json.dump(data, writeItemsFolder)
            newId = int(id) + 1

        writeItemId = open(__item_id_path__, 'w')
        writeItemId.write(str(newId))
    
    @staticmethod
    def fetchAll():
        item_file_names = os.listdir(__items_folder__)
        items = []
        for file_name in item_file_names:
            readItemsFolder = open(__items_folder__+'/'+str(file_name), 'r')
            items.append(readItemsFolder.read())
        return items

    @staticmethod
    def findById(id):
        readItemsFolder = open(__items_folder__+'/'+str(id)+'.json', 'r')
        return readItemsFolder.read()

    @staticmethod
    def find(key, value):
        items = Item.fetchAll()
        filteredItems = []

        for item in items:
            if json.loads(item)[key] == value:
                filteredItems.append(item)
        
        return filteredItems

def item_create(name, price, selling_price):
    item = Item(name, price, selling_price)
    item.save()

    
def item_all():
    allItems = Item.fetchAll()
    print(allItems)

def item_view(id):
    item = Item.findById(id)
    print(item)

def item_search(key, value):
    items = Item.find(key, value)
    print(items)
