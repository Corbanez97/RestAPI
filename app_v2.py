from attr import fields
from flask import Flask, request
from flask_restful import Api, Resource, reqparse, fields, marshal_with

from flask_sqlalchemy import SQLAlchemy #Create Database

#initializes the RestfulAPI
app = Flask(__name__)
api = Api(app)

db_uri = 'sqlite:///database.db'

#initializes Database
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
db = SQLAlchemy(app)

class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key = True) #requires that the primary key ordered from 1 to N
    name = db.Column(db.String(50), nullable = False)
    age = db.Column(db.Integer, nullable = False)
    job = db.Column(db.String(50), nullable = True)

    def __repr__(self):
        return f"{id}(name = {name}, age = {age}, job = {job})"

#db.create_all()

names_put_args = reqparse.RequestParser()
#one could add required arg to show help message in case of null argument
names_put_args.add_argument("name", type = str, help = "Name of the User") 
names_put_args.add_argument("age", type = int, help = "Age of the User")
names_put_args.add_argument("job", type = str, help = "Job of the User")

#setting fields
resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'age': fields.Integer,
    'job': fields.String
}

##RESOURCES
class UserLog(Resource):
    
    #Get data from server
    @marshal_with(resource_fields) #takes return values and serializes with variable resource_fields
    def get(self, user_id):
        result = UserModel.query.get(user_id)
        return result #response must be serializable, i.e., json formats
    
    #Update data from server
    def put(self, user_id):
        return{"Hello World": 200}

    #Post data on server
    def post(self, user_id):
        print(request.method)
        print(request.form)
        args = names_put_args.parse_args()
        #Create user
        user = UserModel(id = user_id, name = args["name"], age = args["age"], job = args["job"]) 
        #Add user to db
        db.session.add(user)
        #Commit changes to db
        db.session.commit()
        return "", 201 #201 is CREATED

    #Remove data from server
    def delete(self, user_id):        
        return "", 204 #204 is DELETED SUCCESSFULLY
        #Delete does not return a serializable response
        
##we have also requested from the user a parameter with the appended section <>
api.add_resource(UserLog, "/userlog/<int:user_id>")    #determine the root of the HelloWorld resource
                                                            #we can access this resource via the url /userlog

if __name__ == "__main__":
    app.run(debug = True) #debug only for DEV and QA env!