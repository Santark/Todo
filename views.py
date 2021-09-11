from flask import request, abort
from validation import *
from handler.listHandler import *
from handler.userHandler import *
from handler.argsHandler import *
from app import app

@app.route('/createUser', methods=['POST'])
def createUser():
    username, email, password, phoneNo = getPostArgs(request, "username", "email", "password", "phoneNo")
    try:
    	groupId = request.json["groupId"]
    except:
    	groupId = None
    #handling 400 scenarios
    if not isInt(phoneNo):
        abort(400)
    return createNewUser(username, email, password, phoneNo)

@app.route('/getUser', methods=['GET'])
def getUser():
    user_id = getArgs(request, "user_id")[0]
    #handling 400 scenarios
    if not isInt(user_id):
        abort(400)
    return getUserDetails(user_id)

@app.route('/list', methods=['POST'])
def createNewList():
	userId, data, name = getPostArgs(request, "userId", "data", "name")
    # handling 400 scenarios
	if not isInt(userId): 
	    abort(400)
	return createListItem(userId, data, name)

@app.route('/list', methods=['GET'])
def getlistDetails():
    user_id, list_id = getArgs(request, "userId", "listId")
    #handling 400 scenarios
    if not isInt(user_id):
        abort(400)
    if not isInt(list_id):
        abort(400)
    return getList(user_id, list_id)

@app.route('/list', methods=['PUT'])
def handleUpdateExpense():
    user_id, list_id, data, name = getPutArgs(request, "userId", "listId", "data", "name")
    #handling 400 scenarios
    if not isInt(user_id):
        abort(400)
    if not isInt(list_id):
        abort(400)
    return updateList(user_id, list_id, data, name)

@app.route('/list', methods=['DELETE'])
def handleDeleteList():
    user_id, list_id = getArgs(request, "userId", "listId")
    #handling 400 scenarios
    if not isInt(user_id):
        abort(400)
    if not isInt(list_id):
        abort(400)
    return deleteList(user_id, list_id)
