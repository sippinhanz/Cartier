from flask import Flask, render_template, request
import datetime
import time

app = Flask(__name__)
var1 = 0
list = {}
def Js(id):
    return [{"href": "/prec","type": "GET"},{"href": "/prec1/<id>","type": "GET"},
            {"href": "/vytvor","type": "POST"},{"href": "/smaz/<id>","type": "DELETE"},
            {"href": "/uprav/<id>","type": "PUT"}]

@app.route('/api/v2/prec', methods=["GET"])
def prec():
    if(len(list) == 0 ):
        return {"error":"Dic is empty"}
    else:
        return {"AP": list, "linky": Js(1)}

@app.route('/api/v2/prec1/<id>', methods=["GET"])
def prec1(id):
    if(len(list) == 0 ):
        return {"error":"Dic is empty"}
    elif(list.__contains__(id) is False):
        return {"error":"Dic doesnt contain inserted id"}
    else:
        return {"AP": list[int(id)], "linky": Js(id)}

@app.route('/api/v2/vytvor', methods=["POST"])
def vytvor():
    global var1
    var2 = request.get_json()
    item = var2["AP"]
    list[var1] = item
    var1 += 1
    return {"AP": "rdy", "linky": Js(1)}

@app.route('/api/v2/smaz/<id>', methods=["DELETE"])
def smaz(id):
    if(list.__contains__(id) is False):
        return {"error":"Dic doesnt contain inserted id"}
    else:
        list.pop(int(id))
        return {"AP": "rdy", "linky": Js(id)}

@app.route('/api/v2/uprav/<id>', methods=["PUT"])
def uprav(id):
    if(list.__contains__(id) is False):
        return {"error":"Dic doesnt contain inserted id"}
    else:
        var2 = request.get_json()
        item = var2["text"]
        list[int(id)] = item
        return {"AP": "rdy", "linky": Js(id)}

@app.route('/api/v2/doc')
def dokumenace():
    return render_template('dokumentace.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)




## navrh delete_all
##opravit bug v delete zap. cislo
##po smazani vypsat Json prvku
##
##
##

