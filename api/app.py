from flask import Flask, request, jsonify
from src.calculate import Np_Math, Basic_Math
from flask import g

app = Flask(__name__)

a = None
b = None
np_data = None
math_obj = None


@app.route("/")
def index():
    return "Welcome to Calculator app"


@app.route("/initialize", methods=["POST"])
def initialize():
    data = request.json
    global a
    a = data["op1"]
    global b
    b = data["op2"]
    global np_data
    np_data = data["np_data"]
    global math_obj
    math_obj = Np_Math(np_data)
    return jsonify({"result": "Initialized Successfully"})


@app.route("/addition", methods=["GET"])
def addition():

    result = math_obj.add(a, b)
    return result


@app.route("/subtraction", methods=["GET"])
def subtraction():

    result = math_obj.subtract(a, b)
    return result


@app.route("/multiplication", methods=["GET"])
def multiplication():

    result = math_obj.multiply(a, b)
    return result


@app.route("/division", methods=["GET"])
def division():

    result = math_obj.subtract(a, b)
    return result


if __name__ == "__main__":
    # run() method of Flask class runs the application
    # on the local development server.

    app.run()
