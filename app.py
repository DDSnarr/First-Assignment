from flask import Flask
from flask import request
from flask import jsonify
from flask import abort

app = Flask(__name__)

@app.route("/is_even")
def is_even():
    number = request.args.get('number')

    if number is None:
        abort(400, "Enter number=")

    if not number.isnumeric():
        abort(400, 'Input needs to be a numeric value')

    number = int(number)
    
    if number % 2 == 0:
        return jsonify(result=True)
    else:
        return jsonify(result=False)




app.run(port=5000, debug=True)
