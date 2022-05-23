from flask import Flask, request, render_template, jsonify

app=Flask(__name__)

gods=[{'name':'Zeus'},{'name':'Hades'},{'name':'Posedian'},{'name':'Artemis'},{'name':'Hera'},{'name':'Aethna'}]

"""
get method
"""
@app.route('/', methods=['GET'])
def welcome():
    return jsonify({'message':'hello there. how are you ?'})

@app.route('/gods',methods=['GET'])
def greek_gods():
    return jsonify({'gods':gods})

# when name-string is empty gives 404 error
@app.route('/gods/<string:name>',methods=['GET'])
def greek_god(name):
    god=[god for god in gods if god['name']==name]
    return jsonify({'gods':god})

"""
post method
"""
@app.route('/gods',methods=['POST'])
def greek_gods_post():
    new_god={'name':request.json['name']}
    gods.append(new_god)
    return jsonify({'gods':gods})

"""
put method
"""
@app.route('/gods/<string:name>',methods=['PUT'])
def greek_god_put(name):
    new_god=[god for god in gods if god['name']==name]
    new_god[0]['name']=request.json['name']
    return jsonify({'gods':new_god[0]})

"""
delete method
"""
@app.route('/gods', methods=['DELETE'])
def greek_god_delete():
    god_to_be_deleted=request.json['name']
    # if god is not in the list then just return gods
    try:
        gods.remove({'name':god_to_be_deleted})
    except ValueError:
        pass
    return jsonify({'gods':gods})

if __name__=="__main__":
    # to run app in debug mode on port 8000
    app.run(debug=True, port=8000)