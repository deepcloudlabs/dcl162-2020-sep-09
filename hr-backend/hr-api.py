import json

from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
app.config['DEBUG'] = True
cors = CORS(app)

fields = ["identity", "fullName", "iban", "photo", "birthYear", "salary", "department", "fulltime" ]

client = MongoClient("mongodb://localhost:27017")

hr_db = client['hr']  # hr database

employees = hr_db.employees  # employees collection


# http://localhost:4400/hr/api/v1/employees/1
@app.route("/hr/api/v1/employees/<identity>", methods=["GET"])
def getEmployeeByIdentity(identity):
    return jsonify(employees.find_one({"identity": identity}))

# http://localhost:4400/hr/api/v1/employees
@app.route("/hr/api/v1/employees", methods=["GET"])
def getEmployees():
    return json.dumps([emp for emp in employees.find({})])


app.run(host="localhost", port=4400)
