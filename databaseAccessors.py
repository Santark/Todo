from models import User, ToDo
from app import db 
import json

def getUser(user_id):
    """
    To query the db and fetch the user details for a particular id
    """
    try:
        user = User.query.filter(User.user_id == user_id).one()
        return user
    except:
        return None

def addUser(username, email, password, phoneNo):
    user = User(username, email, password, phoneNo)
    db.session.add(user)
    commitToDb()
    return user

def createList(user_id, data, name, date_created):
    try:
        _list = ToDo(user_id, date_created, data, name)
        db.session.add(_list)
        commitToDb()
        return _list
    except:
        return None

def getListItem(user_id, list_id):
    try:
        _list = ToDo.query.filter(ToDo.user_id == user_id).filter(ToDo.list_id == list_id).one()
        return _list
    except Exception as e:
        print(e)
        raise Exception("Error occured")

def deleteListItem(user_id, list_id):
    try:
        _list = ToDo.query.filter(ToDo.user_id == user_id).filter(ToDo.list_id == list_id).delete()
        commitToDb()
    except Exception as e:
        print(e)
        raise Exception("Error occured")

def updateListItem(user_id, list_id, data, name):
    """ """
    try:
        _list = getListItem(user_id, list_id)
        _list.data = data
        _list.name = name
        db.session.add(_list)
        commitToDb()
        return _list
    except:
        raise Exception("Error occured")

def commitToDb():
	""" """
	db.session.commit()