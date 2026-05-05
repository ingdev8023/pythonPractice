from flask import Flask, jsonify, make_response, request

app = Flask(__name__)

data = [
    {
        "id": "3b58aade-8415-49dd-88db-8d7bce14932a",
        "first_name": "Tanya",
        "last_name": "Slad",
        "graduation_year": 1996,
        "address": "043 Heath Hill",
        "city": "Dayton",
        "zip": "45426",
        "country": "United States",
        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff",
    },
    {
        "id": "d64efd92-ca8e-40da-b234-47e6403eb167",
        "first_name": "Ferdy",
        "last_name": "Garrow",
        "graduation_year": 1970,
        "address": "10 Wayridge Terrace",
        "city": "North Little Rock",
        "zip": "72199",
        "country": "United States",
        "avatar": "http://dummyimage.com/148x100.png/dddddd/000000",
    },
    {
        "id": "66c09925-589a-43b6-9a5d-d1601cf53287",
        "first_name": "Lilla",
        "last_name": "Aupol",
        "graduation_year": 1985,
        "address": "637 Carey Pass",
        "city": "Gainesville",
        "zip": "32627",
        "country": "United States",
        "avatar": "http://dummyimage.com/174x100.png/ff4444/ffffff",
    },
    {
        "id": "0dd63e57-0b5f-44bc-94ae-5c1b4947cb49",
        "first_name": "Abdel",
        "last_name": "Duke",
        "graduation_year": 1995,
        "address": "2 Lake View Point",
        "city": "Shreveport",
        "zip": "71105",
        "country": "United States",
        "avatar": "http://dummyimage.com/145x100.png/dddddd/000000",
    },
    {
        "id": "a3d8adba-4c20-495f-b4c4-f7de8b9cfb15",
        "first_name": "Corby",
        "last_name": "Tettley",
        "graduation_year": 1984,
        "address": "90329 Amoth Drive",
        "city": "Boulder",
        "zip": "80305",
        "country": "United States",
        "avatar": "http://dummyimage.com/198x100.png/cc0000/ffffff",
    }
]


@app.route("/")
def index():
    return 'hello world'

@app.route("/no_content")
def no_content():
    return jsonify("No content found"), 204

@app.route("/exp")
def index_explicit():
    res = make_response({'message': 'making a response'})
    res.status_code = 200
    return res

@app.route('/data')
def get_data():
    try:
        if data and len(data) > 0:
            return data
        else:
            return {"message": "Data is empty"}, 500
    except NameError:
        return {"message": "Data not found"}, 404

@app.route('/name_search')
def name_search():

    name = request.args.get('q')
    
    if name is None:
        return {"message" : "Query parameter is missing"}, 400
    if name.strip() == "" or name.isdigit():
        return  {"message" : "Invalid input parameter"}, 422

    for person in data:
        if name.lower() in person["first_name"].lower():
            return person, 200
        
    return {"message": "Person not found"}, 404

@app.route("/count")
def count():
    return {"data count": len(data)}

@app.route("/person/<uuid:unique_id>", methods = ["GET", "DELETE"])
def find_by_uuid(unique_id):
    
    if request.method =="GET":
        for person in data:
            if str(unique_id) in person['id']:
                return person, 200
        return {"message":"Person not found"}, 404
    
    if request.method == "DELETE":
        for person in data:
            if str(unique_id) in person['id']:
                data.remove(person)
                return {"message": f'Person with ID {unique_id} deleted'}, 200
        return {"message":"Person not found"}, 404

@app.route("/person", methods=["POST"])
def add_by_uuid():
    person = request.json

    if not person:
        return {"message" : "Invalid input parameter"}, 422
    
    try:
        data.append(person)
    except NameError:
        return {"message":"data not defined"}, 500

    return {"message": f'{person["id"]}'}, 200

@app.errorhandler(404)
def api_not_found(error):
    return {"message":"API not found"}, 404

@app.route("/test500")
def test500():
    raise Exception("Forced exception for testing")

