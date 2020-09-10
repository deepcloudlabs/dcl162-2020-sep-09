def extract_employee_from_request(request,fields):
    emp = {}
    for field in fields:
        if field in request.json:
            emp[field] = request.json[field]
    emp["_id"] = emp["identity"]
    return emp