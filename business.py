class Product:
    def __init__(self, productID=0, name="", price=0.0, discountPercent=0, quantity=0):
            self.productID = productID
            self.name = name
            self.price = price
            self.discountPercent = discountPercent
            self.quantityAvailable = quantity

    def getDiscountAmount(self):
        discountAmount = self.price * self.discountPercent / 100
        return round(discountAmount, 2)

    def getDiscountPrice(self):
        discountPrice = self.price - self.getDiscountAmount()
        return round(discountPrice, 2)

class LineItem:
    def __init__(self, product=None, quantity=1):
            self.product = product
            self.quantity = int(quantity)

    def getTotal(self):
        total = self.product.getDiscountPrice() * self.quantity
        return round(total, 2)

    def updateQuantity(self, newQuantity):
        self.quantity = int(newQuantity)

class Cart:
    def __init__(self):
        self.__lineItems = []

    def addItem(self, item):
        self.__lineItems.append(item)

    def removeItem(self, index):
        self.__lineItems.pop(index)

    def getTotal(self):
        total = 0.0
        for item in self.__lineItems:
            total += item.getTotal()
        return round(total, 2)

    def getItemCount(self):
        return len(self.__lineItems)

    def decreaseItemQuantity(self, id):
        i=0
        for item in self.__lineItems:
            if int(item.product.productID) == id:
                if item.quantity>1:
                    item.updateQuantity(item.quantity-1)
                else:
                    self.removeItem(i)
            i+=1

    def increaseItemQuantity(self, id):
        for item in self.__lineItems:
            if int(item.product.productID) == id:
                item.updateQuantity(item.quantity+1)

    def removeItemByProductID(self, id):
        i=0
        for item in self.__lineItems:
            if int(item.product.productID) == id:
                self.removeItem(i)
            i+=1

    def addItemByProductID(self, id, quantity, products):
        quantity = int(quantity)
        inCart = False
        for item in self.__lineItems:
            if int(item.product.productID) == id:
                item.updateQuantity(item.quantity+quantity)
                inCart = True
        if not inCart and quantity>0:
            self.addItem(LineItem(products[id-1], quantity))

    def checkout(self):
        for item in self.__lineItems:
            item.product.quantityAvailable = item.product.quantityAvailable- item.quantity
            print(item.product.quantityAvailable)
        self.__lineItems = []

    def __iter__(self):
        self.__index = -1
        return self

    def __next__(self):
        self.__index += 1
        if self.__index >= len(self.__lineItems):
            raise StopIteration
        lineItem = self.__lineItems[self.__index]
        return lineItem

class Order:
    def __init__(self):
        self.__lineItems = []

    def __init__(self, cart):
        self.__lineItems = []
        for item in cart:
            self.addItem(item)

    def addItem(self, item):
        self.__lineItems.append(item)

    def removeItem(self, index):
        self.__lineItems.pop(index)

    def getTotal(self):
        total = 0.0
        for item in self.__lineItems:
            total += item.getTotal()
        return round(total, 2)

    def getItemCount(self):
        return len(self.__lineItems)

    def __iter__(self):
        self.__index = -1
        return self

    def __next__(self):
        self.__index += 1
        if self.__index >= len(self.__lineItems):
            raise StopIteration
        lineItem = self.__lineItems[self.__index]
        return lineItem
