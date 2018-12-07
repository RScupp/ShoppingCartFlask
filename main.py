from flask import Flask, flash, redirect, render_template, request, session, abort
import db
from business import Product, LineItem, Cart, Order

app = Flask(__name__)

products = db.get_products()
cart = Cart()

@app.route("/")
def productList():
    return render_template('products.html', products=products, cart=cart)

@app.route("/cart")
def cartPage():
    return render_template('cart.html', cart=cart)

@app.route("/checkout", methods=['POST'])
def checkoutPage():
    order = Order(cart)
    cart.checkout()
    db.updateItems(products)
    return render_template('checkout.html', order=order)

@app.route('/increaseQuantity/<int:id>')
def increaseQuantity(id=None):
    if id is not None:
        cart.increaseItemQuantity(id)
    return "nothing"

@app.route('/decreaseQuantity/<int:id>')
def decreaseQuantity(id=None):
    if id is not None:
        cart.decreaseItemQuantity(id)
    return "nothing"

@app.route('/removeItem/<int:id>')
def removeItem(id=None):
    if id is not None:
        cart.removeItemByProductID(id)
    return "nothing"

@app.route('/addToCart/<int:id>/<quantity>')
def addToCart(id=None, quantity=None):
    if id is not None and quantity is not None:
        cart.addItemByProductID(id, quantity, products)
    return "nothing"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port="8100")
