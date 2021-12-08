from flask import jsonify,Flask,request

app = Flask(__name__)
@app.route("/")
def contacts():
    return "These are the contact lists."

details = [{"id":1,"Name":"Rishi","Contact":"11-03947443","City":"New Delhi","done":False},{"id":2,"Name":"Rohit","Contact":"11-03445789","City":"Chennai","done":False}]
@app.route("/add-data",methods = ["POST"])
def addtask():
    if not request.json():
        return jsonify({
            "status":"error",
            "message":"Please provide your data."
        },400)
    contact = {
        "id": details[-1]["id"]+1,
        "Name": request.json["Name"],
        "Contact": request.json.get("Contact",""),
        "Place": request.json.get("Place",""),
        "done": False
    }
    details.append(contact)
    return jsonify({
        "status":"success",
        "message":"Data added successfully!"
    })
@app.route("/get-data")
def gettask():
    return jsonify({"data":details})

if(__name__=="__main__"):
    app.run(debug=True)

    
