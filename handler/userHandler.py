from databaseAccessors import *
import json

def createNewUser(username, email, password, phoneNo):
    user = addUser(username, email, password, phoneNo)
    return (json.dumps({"success": True, "user_id": str(user.user_id)}), 200)
    
def getUserDetails(user_id):
    user = getUser(user_id)
    if user != None:
      return (json.dumps({"success": True, "userId": str(user.user_id), "userDetails": user.getUserDetails()}), 200)
    return (json.dumps({"success": False}), 404)