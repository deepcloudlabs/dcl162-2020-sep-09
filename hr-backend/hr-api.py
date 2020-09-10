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
curl -X POST http://localhost:4400/hr/api/v1/employees -H "Content-Type: application/json" -H "Accept: application/json" -d "{\"identity\": \"2\", \"fullName\": \"kate austen\", \"iban\": \"tr2\", \"photo\" : null, \"birthYear\": 1986, \"salary\": 200000, \"department\": \"SALES\", \"fulltime\": true}"
curl -X PUT http://localhost:4400/hr/api/v1/employees/2 -H "Content-Type: application/json" -H "Accept: application/json" -d "{\"identity\": \"2\", \"fullName\": \"kate austen\", \"iban\": \"tr2\", \"photo\" : null, \"birthYear\": 1986, \"salary\": 200000, \"department\": \"SALES\", \"fulltime\": true}"
curl -X PATCH http://localhost:4400/hr/api/v1/employees/2 -H "Content-Type: application/json" -H "Accept: application/json" -d "{\"fulltime\": true}"
curl -X DELETE http://localhost:4400/hr/api/v1/employees/2 -H "Accept: application/json"
"""


@app.route("/hr/api/v1/employees", methods=["POST"])
def addEmployee():
    employees.insert_one(extract_employee_from_request(request, fields))
    return jsonify({"status": "ok"})


@app.route("/hr/api/v1/employees/<identity>", methods=["PUT", "PATCH"])
def updateEmployee(identity):
    emp = extract_employee_from_request(request, fields)
    emp["_id"] = identity
    employee = employees.find_one_and_update(
        {"_id": identity},
        {"$set": emp},
        upsert=False
    )
    return jsonify(employee)


@app.route("/hr/api/v1/employees/<identity>", methods=["DELETE"])
def removeEmployee(identity):
    employee = employees.find_one({"_id": identity})
    employees.delete_one({"_id": identity})
    return jsonify(employee)


app.run(host="localhost", port=4400)
