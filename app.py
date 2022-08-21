from flask import Flask
from flask import request
from flask import jsonify
from flask import abort

app = Flask(__name__)

@app.get("/is_even")
def is_even():
    number = request.args.get('number')

    if number is None:
        return jsonify(error="Enter number="), 400

    if not number.isnumeric():
        return jsonify(error="Input needs to be a numeric value"), 400

    number = int(number)

    if number % 2 == 0:
        return jsonify(result=True)
    else:
        return jsonify(result=False)


@app.get("/is_odd")
def is_odd():
    number = request.args.get('number')

    if number is None:
        return jsonify(error="Enter number="), 400

    if not number.isnumeric():
        return jsonify(error="Input needs to be a numeric value"), 400

    number = int(number)

    if number % 2 != 0:
        return jsonify(result=True)
    else:
        return jsonify(result=False)


app.run(port=5000, debug=True)
