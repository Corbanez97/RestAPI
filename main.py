from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort

#initializes the RestfulAPI
app = Flask(__name__)
api = Api(app)

names_put_args = reqparse.RequestParser()
#one could add required arg to show help message in case of null argument
names_put_args.add_argument("name", type = str, help = "Name of the User") 
names_put_args.add_argument("age", type = int, help = "Age of the User")
names_put_args.add_argument("job", type = str, help = "Job of the User")

names = {1001: {"name": "Lucas", "age": 25, "job": "data engineer"}, 
            1002: {"name": "Pedro", "age": 29, "job": "rich"},
                1003: {"name": "Miguel", "age": 22, "job": "dotô"}}

def abort_invalid_id(user_id):
    if user_id not in names:
        abort(404, message = "Invalid user id.") #404 not found. Status is required!

#resources
class UserLog(Resource):
    def get(self, user_id):
        abort_invalid_id(user_id)
        return names[user_id] #response must be serializable, i.e., json formats
    
    def post(self, user_id):
        return{"Hello World": 200}

    def put(self, user_id):
        print(request.method)
        print(request.form)
        args = names_put_args.parse_args()
        names[user_id] = args
        return names[user_id], 201 #201 is CREATED

##we have also requested from the user a parameter with the appended section <>
api.add_resource(UserLog, "/userlog/<int:user_id>")    #determine the root of the HelloWorld resource
                                                            #we can access this resource via the url /helloworld

if __name__ == "__main__":
    app.run(debug = True) #only for DEV and QA env!