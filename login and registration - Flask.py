from flask import Flask, request, render_template,json, url_for
from flask_restful import reqparse, Resource, Api
import json


app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()

USERS ={
    "1": {"username": "martinek", "password": "123456789"},
    "2":{"username": "adamek", "password": "2356897"},
    "3": {"username": "kolobrnda", "password": "1245789"},
    }


class UserList(Resource):

    def load(self):
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        json_data = os.path.join(SITE_ROOT, "static/data", "ID.json")
        data = json.load(open(json_data))
        return render_template('showjson.jade', data=data)

    def get(self):
        return USERS

    def post(self):
        parser.add_argument("username")
        parser.add_argument("password")
        args = parser.parse_args()
        user_id = int(max(USERS.keys())) + 1
        user_id = "%i" % user_id
        USERS[user_id] = {
            "username": args["username"],
            "password": args["password"]
        }
        return USERS[user_id], 201


class User(Resource):
    def get(self, user_id):
        if user_id not in USERS:
            return "not Found", 404
        else:
            return USERS[user_id]

    def put(self, user_id, json_data):
        parser.add_argument("username")
        parser.add_argument("password1")
        parser.add_argument("pasword2")
        args = parser.parse_args()
        if user_id in USERS:
            return "record not Found", 404
        else:
            user = USERS[user_id]
            user["username"] = args["username"] if args["username"] is not None else user["username"]
            user["password1"] = args["password1"] if args["password1"] is not None else user["password1"]
            user["password2"] = args["password2"] if args["password2"] is not None else user["password2"]
            if ["pasword1"] != ["pasword2"]:
                return user, 404
            else:
                 with open("ID.json","w") as file:
                    a = {"username":["username"], "pasword": ["pasword1"]}
                    print(json_data["users"])
                    json_data["users"].append(a)
                    print(json_data["users"])
                    json.dump(json_data, file, indent= 2 )

    def delete(self, user_id):
        if user_id not in USERS:
            return "not found", 404
        else:
            del USERS[user_id]
            return "", 204


api.add_resource(UserList, "/User list/")
api.add_resource(User, "/<user_id>")

if __name__ == "__main__":
    app.run(debug=True)
