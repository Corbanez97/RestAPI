from urllib import response
import requests

BASE = "http://127.0.0.1:5000/" ##Running on FlaskAPI Server

args = {"name": "Lucas", "age": 25, "job": "Data Engineer"}

# response = requests.post(BASE + "userlog/2", args) #test post
# print("Test post: ", response, type(response))

response = requests.get(BASE + "userlog/1") #test get
print("Test get: ", response.json())




