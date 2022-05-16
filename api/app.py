from flask import Flask, request
from src import basic_math.py as bm
from src import np_math.py as nm
app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to Calculator app"

@app.route("/calculate")
def calculate(methods=["POST"]):
    data = request.json
    a = data["op1"]
    b = data["op2"]
    opr = data["opr"]
    np_data = data["np_data"]

    if np_data:
        math_obj = bm(a, b)
    else:
        math_obj = nm(a,b)
    if opr == "+":
        result = math_obj.add()
        return result
    elif opr == "-":
        return math_obj.subtract()
    elif opr == "*":
        return math_obj.mult()
    elif opr =="/":
        return math_obj.divide()


if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()