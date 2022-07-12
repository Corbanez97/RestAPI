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

##VALIDATION
def abort_invalid_id(user_id):
    if user_id not in names:
        abort(404, message = "Invalid user id.") #404 not found. Status is required!
def abort_existing_id(user_id):
    if user_id in names:
        abort(409, message = "Existing user id.")

##RESOURCES
class UserLog(Resource):
    #Get data from server
    def get(self, user_id):
        abort_invalid_id(user_id) #if invalid id abort get
        return names[user_id] #response must be serializable, i.e., json formats
    
    #Update data from server
    def put(self, user_id):
        return{"Hello World": 200}

    #Post data on server
    def post(self, user_id):
        print(request.method)
        print(request.form)
        abort_existing_id(user_id) #if existing id do not create
        args = names_put_args.parse_args()
        names[user_id] = args
        return names[user_id], 201 #201 is CREATED

    #Remove data from server
    def delete(self, user_id):
        abort_invalid_id(user_id)
        del names[user_id]
        return "", 204 #204 is DELETED SUCCESSFULLY
        #Delete does not return a serializable response
        
##we have also requested from the user a parameter with the appended section <>
api.add_resource(UserLog, "/userlog/<int:user_id>")    #determine the root of the HelloWorld resource
                                                            #we can access this resource via the url /userlog

if __name__ == "__main__":
    app.run(debug = True) #debug only for DEV and QA env!