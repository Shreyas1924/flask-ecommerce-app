from flask import Flask, render_template, redirect, url_for, session, request
from models import db, Product, User, Order

app = Flask(__name__)

app.secret_key = "secretkey"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///store.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/products")
def products():

    products = Product.query.all()

    return render_template("products.html", products=products)


@app.route("/add_to_cart/<int:product_id>")
def add_to_cart(product_id):

    cart = session.get("cart", {})

    product_id = str(product_id)

    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1

    session["cart"] = cart

    return redirect(url_for("products"))


@app.route("/cart")
def cart():

    cart = session.get("cart", {})

    products = []

    total = 0

    for product_id, quantity in cart.items():

        product = Product.query.get(int(product_id))

        if product:

            subtotal = product.price * quantity

            total += subtotal

            products.append({
                "product": product,
                "quantity": quantity,
                "subtotal": subtotal
            })

    return render_template("cart.html", products=products, total=total)

@app.route("/checkout")
def checkout():

    cart = session.get("cart", {})

    for product_id, quantity in cart.items():

        product = Product.query.get(int(product_id))

        if product:

            order = Order(
                product_name=product.name,
                price=product.price,
                quantity=quantity,
                total_price=product.price * quantity
            )

            db.session.add(order)

    db.session.commit()

    session["cart"] = {}

    return render_template("checkout_success.html")

@app.route("/orders")
def orders():

    orders = Order.query.all()

    return render_template("orders.html", orders=orders)


@app.route("/remove_from_cart/<int:product_id>")
def remove_from_cart(product_id):

    cart = session.get("cart", {})

    product_id = str(product_id)

    if product_id in cart:
        del cart[product_id]

    session["cart"] = cart

    return redirect(url_for("cart"))

@app.route("/decrease_quantity/<int:product_id>")
def decrease_quantity(product_id):

    cart = session.get("cart", {})

    product_id = str(product_id)

    if product_id in cart:

        cart[product_id] -= 1

        if cart[product_id] <= 0:
            del cart[product_id]

    session["cart"] = cart

    return redirect(url_for("cart"))

@app.route("/increase_quantity/<int:product_id>")
def increase_quantity(product_id):

    cart = session.get("cart", {})

    product_id = str(product_id)

    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1

    session["cart"] = cart

    return redirect(url_for("cart"))


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        new_user = User(username=username, email=email, password=password)

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("home"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(email=email, password=password).first()

        if user:
            session["user_id"] = user.id
            return redirect(url_for("home"))

        else:
            return "Invalid credentials"

    return render_template("login.html")


@app.route("/logout")
def logout():

    session.pop("user_id", None)

    return redirect(url_for("home"))


@app.route("/add_product", methods=["GET", "POST"])
def add_product():

    if request.method == "POST":

        name = request.form["name"]
        price = request.form["price"]

        product = Product(name=name, price=price)

        db.session.add(product)
        db.session.commit()

        return redirect(url_for("products"))

    return render_template("add_product.html")


if __name__ == "__main__":
    app.run(debug=True)