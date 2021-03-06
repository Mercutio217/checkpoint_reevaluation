from flask import Flask, render_template, request, redirect, url_for
from controller.Product_controller import Product_Controller
from model.Product import Product

app = Flask(__name__)
my_controller = Product_Controller()


@app.route("/", methods=["GET", "POST"])
def index():
    list_of_products = my_controller.get_product_list()
    return render_template("index.html", list_of_products=list_of_products)


@app.route("/add", methods=["GET", "POST"])
def add_product():
    if request.method == "GET":
        return render_template("add_product.html")
    else:
        new_product = Product(request.form["name"], request.form["description"], request.form["price"])
        my_controller.add_product(new_product)
        return redirect("index")


@app.route("/remove/<int:product_id>", methods=["GET", "POST"])
def remove_product(product_id):
    my_controller.remove_product(product_id)
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run(debug=True)
