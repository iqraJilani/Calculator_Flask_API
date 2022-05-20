from flask import Flask, request, jsonify
from src.Basic_Math import BasicMath
from src.Np_Math import NpMath
from flask import g

app = Flask(__name__)

math_obj = None
np_data = None


@app.route("/")
def index():
    return "Welcome to Calculator app"


@app.route("/initialize", methods=["POST"])
def initialize():
    data = request.json
    a = data["op1"]
    b = data["op2"]
    global np_data
    np_data = data["np_data"]
    global math_obj
    math_obj = NpMath(a, b)
    return jsonify({"result": "Initialized Successfully"})


@app.route("/addition", methods=["GET", "POST"])
def addition():

    if request.method == "GET":
        global np_data
        result = math_obj.add(np_data)
    else:
        data = request.json
        a = data["op1"]
        b = data["op2"]
        np_data = data["np_data"]
        result = math_obj.add(np_data, a, b)

    return result


@app.route("/subtraction", methods=["GET", "POST"])
def subtraction():

    if request.method == "GET":
        global np_data
        result = math_obj.add(np_data)
    else:
        data = request.json
        a = data["op1"]
        b = data["op2"]
        np_data = data["np_data"]
        result = math_obj.subtract(np_data, a, b)
    return result


@app.route("/multiplication", methods=["GET", "POST"])
def multiplication():

    if request.method == "GET":
        global np_data
        result = math_obj.add(np_data)
    else:
        data = request.json
        a = data["op1"]
        b = data["op2"]
        np_data = data["np_data"]
        result = math_obj.multiply(np_data, a, b)
    return result


@app.route("/division", methods=["GET", "POST"])
def division():

    if request.method == "GET":
        global np_data
        result = math_obj.add()
    else:
        data = request.json
        a = data["op1"]
        b = data["op2"]
        np_data = data["np_data"]
        result = math_obj.divide(np_data, a, b)
    return result


if __name__ == "__main__":
    # run() method of Flask class runs the application
    # on the local development server.

    app.run(host="0.0.0.0")
