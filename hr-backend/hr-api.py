import json
from hr.utility import extract_employee_from_request
from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
app.config['DEBUG'] = True
cors = CORS(app)

fields = ["identity", "fullName", "iban", "photo", "birthYear", "salary", "department", "fulltime"]

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


"""
set c:\DEVEL\stage\opt\curl-7.45.0\bin;%PATH%
curl -X POST http://localhost:4400/hr/api/v1/employees -H "Content-Type: application/json" -H "Accept: application/json" -d "{\"identity\": \"1\", \"fullName\": \"jack bauer\", \"iban\": \"tr1\", \"photo\" : null, \"birthYear\": 1956, \"salary\": 100000, \"department\": \"IT\", \"fulltime\": true}"
"""


@app.route("/hr/api/v1/employees", methods=["POST"])
def addEmployee():
    employees.insert_one(extract_employee_from_request(request, fields))
    return jsonify({"status": "ok"})


app.run(host="localhost", port=4400)
