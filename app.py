from flask import Flask, request, jsonify
import database 
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World'

# Done
@app.route('/find' , methods=['GET'])
def find():
    nogun = request.args.get('nogun')
    jsonData = database.get_data(nogun)
    return jsonify(jsonData)

# Done
@app.route('/alldata',methods=['GET'])
def get():
    print('have get request')
    jsonData = database.get_alldata()
    return jsonify(jsonData)

# Done
@app.route('/pickup',methods=['GET'])
def pickup():
    print('have get request')
    jsonData = int(database.get_pickup()[0])
    return jsonify(jsonData)

#Done
@app.route('/lost',methods=['GET'])
def lost():
    print('have get request')
    jsonData = int(database.get_lost()[0])
    return jsonify(jsonData)

# Done
@app.route('/broken',methods=['GET'])
def broken():
    print('have get request')
    jsonData = int(database.get_broken()[0])
    return jsonify(jsonData)

# Done
@app.route('/remaining',methods=['GET'])
def remaining():
    print('have get request')
    jsonData = int(database.get_remaining()[0])

    return jsonify(jsonData)

# Done
@app.route('/insert', methods=['POST'])
def insert():
    uname = request.args.get('uname')
    pickup = request.args.get("pickup")
    broken = request.args.get('broken')
    lost = request.args.get("lost")
    remaining = request.args.get("remaining")
    nogun = request.args.get("nogun")
    database.insert_data(uname, pickup, broken, lost, remaining, nogun)
    return jsonify({'message': "Insert success"})

# Done
@app.route('/update' , methods=['GET'])
def update():
    # uname = request.args.get('uname')
    pickup = request.args.get('pickup')
    broken = request.args.get('broken')
    lost = request.args.get("lost")
    remaining = request.args.get("remaining")
    nogun = request.args.get("nogun")
    database.update_data(pickup, broken, lost, remaining, nogun)
    return jsonify({'message' : "Update success"})

# Done
@app.route('/delete' , methods=['DELETE'])
def delete():
    nogun = request.args.get('nogun')
    database.delete_data(nogun)
    return jsonify({'message' : " Delete success"})

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=5000, debug=True)
