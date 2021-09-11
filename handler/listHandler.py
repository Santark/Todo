from databaseAccessors import *
from flask import abort
import json
from datetime import date

def createNewList(user_id, data, name):
	date_created = str(date.today())
	_list = createList(user_id, data, name, date_created)
	return (json.dumps({"success": True, "listId": str(_list.list_id)}), 200)

def getList(user_id, list_id):
	try:
		_list = getListItem(user_id, list_id)
		return (json.dumps({"success": True, "listId": str(_list.list_id), "listDetails": _list.getDetails()}), 200)
	except:
		return (json.dumps({"success": False}), 404)

def updateList(user_id, list_id, data, name):
	try:
		_list = updateListItem(user_id, list_id, data, name)
		return (json.dumps({"success": True}), 200)
	except:
		return (json.dumps({"success": False}), 404)

def deleteList(user_id, list_id):
	try:
		deleteListItem(user_id, list_id)
		return (json.dumps({"success": True}), 200)
	except:
		return (json.dumps({"success": False}), 404)

		