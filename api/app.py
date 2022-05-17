from flask import Flask, request, jsonify
from src.calculate import Np_Math, Basic_Math

app = Flask(__name__)


@app.route('/')
def index():
    return "Welcome to Calculator app"


@app.route('/calculate', methods=["POST"])
def calculate():
    data = request.json
    a = data["op1"]
    b = data["op2"]
    opr = data["opr"]
    np_data = data["np_data"]

    if np_data:
        math_obj = Np_Math()
    else:
        math_obj = Basic_Math()


    if opr == "+":
        result = math_obj.add(a, b)
    elif opr == "-":
        result =  math_obj.subtract(a, b)
    elif opr == "*":
        result =  math_obj.multiply(a, b)
    elif opr == "/":
        result =  math_obj.divide(a, b)

    ans_dict = {"ans": result}
    return jsonify(ans_dict)


if __name__ == "__main__":
    # run() method of Flask class runs the application
    # on the local development server.


    app.run(host='0.0.0.0')
