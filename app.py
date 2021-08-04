
from flask import Flask, jsonify, request
from flask_jwt import jwt_required
import controller
from db import main

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'super-secret'


@app.route('/register/', methods=["POST"])
def user_registration():
     first_name = request.form['first_name']
     last_name = request.form['last_name']
     mail = request.form['mail']
     username = request.form['username']
     password = request.form['password']
     result = controller.insert_user(first_name,last_name,mail,username,password)
     return jsonify(result)

@app.route('/login/', methods=["POST"])
def login_user():
    result = controller.get_users()
    return jsonify(result)

@app.route('/show-products', methods=["GET"])
def display_products():
    items = controller.get_products()
    return jsonify(items)

@app.route("/add-product/", methods=["POST"])
def insert_product():
    product_details = request.get_json()
    title = product_details["title"]
    content = product_details["content"]
    uses = product_details["uses"]
    result = controller.insert_product(title, content, uses)
    return jsonify(result)

@app.route("/view-product/<product_id>", methods=["GET"])
def get_product_by_id(product_id):
    product = controller.get_by_id(product_id)
    return jsonify(product)

@app.route("/edit-product/<product_id>", methods=["PUT"])
def update_product():
    product_details = request.get_json()
    title = product_details["title"]
    content = product_details["content"]
    uses = product_details["uses"]
    result = controller.update_product(title, content, uses)
    return jsonify(result)


@app.route("/delete-product/<product_id>", methods=["DELETE"])
def delete_product(product_id):
    result = controller.delete_product(product_id)
    return jsonify(result)


@app.after_request
def after_request(response):
    response.headers["Access-Control-Allow-Origin"] = "http://localhost"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
    return response


if __name__ == "__main__":
    app.run(host='localhost', port=8000, debug=False)
