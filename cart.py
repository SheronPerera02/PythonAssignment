import os
import json

__cart_folder__ = 'db/cart/'
__item_id_path__ = 'db/ids/cart_item_id'
__session_file__ = 'db/session'
__items_folder__ = 'db/items/'

class Cart:

    @staticmethod
    def addToCart(itemId, qty):
        sessionFile = open(__session_file__, 'r')
        loggedUser = sessionFile.read()

        if loggedUser == '':
            print('You need to sign in first')
        else:
            itemFileList = os.listdir(__items_folder__)

            exists = False

            for itemFile in itemFileList:
                if itemFile == itemId+'.json':
                    exists = True
            
            if exists:
        
                fileNameList = os.listdir(__cart_folder__)

                itemExisted = False

                for fileName in fileNameList:
                    cartFile = open(__cart_folder__+fileName, 'r')
                    cartItem = json.load(cartFile)
                    if cartItem['itemId'] == itemId and cartItem['userId'] == loggedUser:
                        cartFile = open(__cart_folder__+fileName, 'w')
                        cartItem['qty'] += int(qty)
                        json.dump(cartItem, cartFile)
                        itemExisted = True
                        print('Updated the cart')
                        break

                if itemExisted == False:
                    cartItemIdFile = open(__item_id_path__, 'r')
                    cartItemId = cartItemIdFile.read()
                    
                    if cartItemId == '':
                        cartItemId = '1'
                    
                    data = {
                        'userId': loggedUser,
                        'itemId': itemId,
                        'qty': int(qty),
                    }

                    cartFile = open(__cart_folder__+cartItemId+'.json', 'w')
                    json.dump(data, cartFile)

                    cartItemIdFile = open(__item_id_path__, 'w')
                    cartItemIdFile.write(str(int(cartItemId) + 1))
                    print('Added to the cart')
            else:
                    print('No item in such id')
    @staticmethod
    def removeFromCart(itemId):
        sessionFile = open(__session_file__, 'r')
        loggedUser = sessionFile.read()

        if loggedUser == '':
            print('You need to sign in first')
        else:
            pass

                     
def cart_add(itemId, qty):
    Cart.addToCart(itemId, qty)

def cart_remove(itemId):
    Cart.removeFromCart(itemId)