from app import db 
import json

"""
CREATE TABLE user (
	user_id INTEGER NOT NULL,
	username VARCHAR(64),
	email VARCHAR(100),
	password VARCHAR(100),
	"phoneNo" VARCHAR(100),
	PRIMARY KEY (user_id)
);
"""
class User(db.Model):
    # unique id
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # user info like name, email
    username = db.Column(db.String(64))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))
    phoneNo = db.Column(db.String(100))
    # user wallet

    def __init__(self, username, email, password, phoneNo):
        self.username = username
        self.email = email
        self.password = password
        self.phoneNo = phoneNo

    def getUserDetails(self):
        return {
            "user_id": self.user_id,
            "username": self.username,
            "email": self.email,
            "phoneNo": self.phoneNo,
            "password": self.password,
        }

    def toString(self):
        return json.dumps(self.getUserDetails())

"""
CREATE TABLE to_do (
	list_id INTEGER NOT NULL,
	user_id INTEGER,
	data TEXT,
	date_created VARCHAR(264),
	name VARCHAR(264),
	PRIMARY KEY (list_id)
);
"""
class ToDo(db.Model):
    list_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer)
    data = db.Column(db.Text())
    date_created = db.Column(db.String(264))
    name = db.Column(db.String(264))

    def __init__(self, user_id, date_created, data, name):
        self.user_id = user_id
        self.data = data
        self.date_created = date_created
        self.name = name

    def getDetails(self):
        return {
            "user_id": self.user_id,
            "data": json.loads(self.data),
            "date_created": self.date_created,
            "name": self.name
        }

    def toString(self):
        return json.dumps(self.getDetails())

if __name__ == "__main__":
    print "Creating database tables..."
    db.create_all()
    print "Done!"
