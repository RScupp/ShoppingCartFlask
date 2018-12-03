from flask import Flask, flash, redirect, render_template, request, session, abort
import db
from business import Product, LineItem, Cart

app = Flask(__name__)

products = db.get_products()
cart = Cart()

@app.route("/")
def productList():
    return render_template('products.html', products=products)

@app.route("/cart")
def cartPage():
    return render_template('cart.html', cart=cart)

@app.route("/checkout", methods=['POST'])
def checkoutPage():
    return render_template('checkout.html', cart=cart)

@app.route('/increaseQuantity/<int:id>')
def increaseQuantity(id=None):
    if id is not None:
        for item in cart:
            if int(item.product.productID) == id:
                item.updateQuantity(item.quantity+1)
    return "nothing"

@app.route('/decreaseQuantity/<int:id>')
def decreaseQuantity(id=None):
    if id is not None:
        i=0
        for item in cart:
            if int(item.product.productID) == id:
                if item.quantity>1:
                    item.updateQuantity(item.quantity-1)
                else:
                    cart.removeItem(i)
            i+=1
    return "nothing"

@app.route('/removeItem/<int:id>')
def removeItem(id=None):
    if id is not None and cart.getItemCount() > 0:
        i=0
        for item in cart:
            if int(item.product.productID) == id:
                cart.removeItem(i)
            i+=1
    return "nothing"

@app.route('/addToCart/<int:id>/<quantity>')
def addToCart(id=None, quantity=None):
    if id is not None and quantity is not None:
        quantity = int(quantity)
        inCart = False
        for item in cart:
            if int(item.product.productID) == id:
                item.updateQuantity(item.quantity+quantity)
                inCart = True
        if not inCart and quantity>0:
            cart.addItem(LineItem(products[id-1], quantity))
    return "nothing"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port="8100")
