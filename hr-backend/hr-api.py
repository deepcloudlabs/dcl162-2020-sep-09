from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.config['DEBUG'] = True
cors = CORS(app)

# http://localhost:4400/hr/api/v1/employees/1
@app.route("/hr/api/v1/employees/1", methods=["GET"])
def getEmployees():
    return jsonify({"fullname": "Jack Bauer"})


app.run(host="localhost", port=4400)
