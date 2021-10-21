
__cart_folder__ = 'db/cart/'
__item_id_path__ = 'db/ids/cart_item_id'

class Cart:

    @staticmethod
    def addToCart(itemId, qty):
        readFile = open('')
        data = {
            'itemId': itemId,
            'qty': qty,
        }

        cartItem = open(__cart_folder__+itemId+'.json')

        print(cartItem)


        # readItemId = open(__item_id_path__, 'r')
        # id = readItemId.read()
        # newId  = 0

        # if id == '':
        #     writeItemsFolder = open(__items_folder__+'/1.json', 'w')
        #     json.dump(data, writeItemsFolder)
        #     newId = 2
        # else:
        #     writeItemsFolder = open(__items_folder__+'/'+str(id)+'.json', 'w')
        #     json.dump(data, writeItemsFolder)
        #     newId = int(id) + 1

        # writeItemId = open(__item_id_path__, 'w')
        # writeItemId.write(str(newId))

def cartAdd(itemId, qty):
    Cart.addToCart(itemId, qty)