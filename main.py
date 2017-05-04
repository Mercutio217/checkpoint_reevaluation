from flask import Flask, render_template, request
from controller.Product_controller import Product_Controller

app = Flask(__name__)
my_controller = Product_Controller()


@app.route("/", methods=["GET", "POST"])
def index():
    list_of_products = my_controller.get_product_list()
    return render_template("index.html", list_of_products=list_of_products)

@app.route("/add", methods=["GET", "POST"])
def add_prolduct():
    if request.method == "GET":
        render_template("add_product.html")
    else:



if __name__ == '__main__':
    app.run(debug=True)
