import db

def newItem(id, name, price, discountPercent, quantity):
    item = []
    item.append(id)
    item.append(name)
    item.append(price)
    item.append(discountPercent)
    item.append(quantity)
    return item

if __name__ == "__main__":
    itemList = []
    itemList.append(newItem(1, "Brown rice", 2.99, 10, 5))
    itemList.append(newItem(2, "Walnuts", 3.99, 0, 5))
    itemList.append(newItem(3, "Bean threads", 1.99, 10, 15))
    itemList.append(newItem(4, "Wasabi", 2.99, 5, 5))
    itemList.append(newItem(5, "Red chile powder", 1.99, 5, 5))
    itemList.append(newItem(6, "Oregano", 1.99, 15, 5))
    itemList.append(newItem(7, "Corn flour", 1.99, 15, 5))
    itemList.append(newItem(8, "Snap peas", 3.99, 5, 15))
    itemList.append(newItem(9, "Turnips", 4.99, 15, 5))
    itemList.append(newItem(10, "Feta cheese", 2.99, 10, 5))
    itemList.append(newItem(11, "Capers", 2.99, 0, 20))
    itemList.append(newItem(12, "Avocados", 2.99, 15, 5))
    itemList.append(newItem(13, "Cider", 4.99, 0, 5))
    itemList.append(newItem(14, "White chocolate", 3.99, 10, 5))
    itemList.append(newItem(15, "Potato chips", 2.99, 5, 15))
    itemList.append(newItem(16, "Tomato puree", 1.99, 0, 20))
    itemList.append(newItem(17, "Blue cheese", 5.99, 10, 20))
    itemList.append(newItem(18, "Alligator", 2.99, 15, 5))
    itemList.append(newItem(19, "Bacon", 5.99, 0, 20))
    itemList.append(newItem(20, "Tomato sauce", 1.99, 10, 10))
    itemList.append(newItem(21, "Onion powder", 2.99, 15, 15))
    itemList.append(newItem(22, "Figs", 4.99, 15, 20))
    itemList.append(newItem(23, "Nectarines", 4.99, 10, 20))
    itemList.append(newItem(24, "Mushrooms", 3.99, 5, 5))
    itemList.append(newItem(25, "Poultry seasoning", 5.99, 0, 5))
    itemList.append(newItem(26, "Ketchup", 5.99, 0, 20))
    itemList.append(newItem(27, "Milk", 1.99, 5, 5))
    itemList.append(newItem(28, "Cannellini beans", 2.99, 15, 15))
    itemList.append(newItem(29, "Kale", 3.99, 5, 5))
    itemList.append(newItem(30, "Brussels sprouts", 5.99, 10, 15))
    db.insertItems(itemList)
