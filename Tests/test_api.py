import requests

json_data = {
 "op1": [[1, 3, 5], [2, 4, 6]],
 "op2": [[7, 9],  [11, 12], [8, 10] ],
 "opr": "*",
 "np_data": True


}

expected_ans = {
    "ans": [
        [
            80,
            95
        ],
        [
            106,
            126
        ]
    ]
}
resp = requests.post('http://127.0.0.1:5000/calculate', json=json_data)

assert str(resp) == "<Response [200]>"




