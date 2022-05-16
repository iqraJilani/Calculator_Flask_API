from flask import Flask, request
from src import calculate

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
        math_obj = calculate.Basic_Math(a, b)
    else:
        math_obj = calculate.np_math(a, b)


    if opr == "+":
        result = math_obj.add(a, b)
        return result
    elif opr == "-":
        return math_obj.subtract(a, b)
    elif opr == "*":
        return math_obj.multiply(a, b)
    elif opr == "/":
        return math_obj.divide(a, b)


if __name__ == "__main__":
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()
