from flask import Flask, request
from flask_restful import reqparse, Resource, Api
import json


app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()

USERS = {
    {"username": "martinek", "password": "123456789"},
    {"username": "adamek", "password": "2356897"},
    {"username": "kolobrnda", "password": "1245789"},
}


class UserList(Resource):

    @property
    def get(self):
        with open("ID.json", "r") as file:
            data = file.read()
            object = json.loads(data)
            print(object)
            return users

    def post(self):
        parser.add_argument("username")
        parser.add_argument("pasSword")
        args = parser.parse_args()
        user_id = int(max(users.keys())) + 1
        user_id = "%i" % user_id
        Users[user_id] = {
            "username": args["username"],
            "password": args["password"]
        }
        return users[user_id], 201


class User(Resource):
    def get(self, user_id):
        if user_id not in USERS:
            return "not Found", 404
        else:
            return user[user_id]

    def put(self, user_id):
        parser.add_argument("username")
        parser.add_argument("password")
        args = parser.parse_args()
        if user_id not in USERS:
            return "record not Found", 404
        else:
            user = users[user_id]
            user["username"] = args["username"] if args["username"] is not None else user["username"]
            user["password"] = args["password"] if args["password"] is not None else user["password"]

    def delete(self, user_id):
        if user_id not in USERS:
            return "not found", 404
        else:
            del USE[user_id]
            return "", 204


api.add_resource(UserList, "/User list/")
api.add_resource(User, "/<user_id>")

if __name__ == "__main__":
    app.run(debug=True)
