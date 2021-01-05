from flask import Flask, url_for, request, abort, redirect, jsonify
from CapitalDAO import capitalDAO

app = Flask(__name__, static_url_path='', static_folder='staticpages')

# curl http://127.0.0.1:5000/
#@app.route('/')
#def index():
    #return "hello"

# curl http://127.0.0.1:5000/capitals
@app.route('/capitals')
def getAll():
    return jsonify(capitalDAO.getAll())

# curl http://127.0.0.1:5000/capitals/1
@app.route('/capitals/<int:id>')
def findById(id):
    return jsonify(capitalDAO.findById(id))

# curl -X POST -H "content-type:application/json" -d "{\"id\":\"1\",\"name\":\"Dublin\", \"country\":\"Ireland\", \"population\": 495781}" http://127.0.0.1:5000/capitals
@app.route('/capitals', methods = ['POST'])
def create():
    if not request.json:
        abort(400)

    capital = {
        "id": request.json["id"], 
        "name": request.json["name"], 
        "country": request.json ["country"], 
        "population": request.json["population"]
        }

    return jsonify(capitalDAO.create(capital))
    #return "served by create"

# curl -X PUT -H "content-type:application/json" -d "{\"name\":\"London\", \"country\":\"United Kingdom\", \"population\": 7500000}" http://127.0.0.1:5000/capitals/1
@app.route('/capitals/<int:id>', methods = ['PUT'])
def update(id):
    foundCapital = capitalDAO.findById(id)
    print(foundCapital)
    if foundCapital == {}:
        return jsonify({}), 404
    currentCapital = foundCapital
    if 'name' in request.json:
        currentCapital['name'] = request.json['name']
    if 'country' in request.json:
        currentCapital['country'] = request.json['country']
    if 'population' in request.json:
        currentCapital['population'] = request.json['population']
    capitalDAO.update(currentCapital)       
    return jsonify(currentCapital)

# curl -X DELETE http://127.0.0.1:5000/capitals/1
@app.route('/capitals/<int:id>', methods = ['DELETE'])
def delete(id):
    capitalDAO.delete(id)
    return jsonify({"done":True})

if __name__=="__main__":
    app.run(debug=True)