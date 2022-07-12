from urllib import response
import requests

BASE = "http://127.0.0.1:5000/" ##Running on FlaskAPI Server

response = requests.get(BASE + "userlog/1001") #test get
print("Test get: ", response.json())

response = requests.get(BASE + "userlog/1004") #test abort invalid id
print("Test get invalid id: ", response.json())

response = requests.put(BASE + "userlog/1001") #test put
print("Test put: ", response.json())

args = {"name": "Paola", "age": 26, "job": "Medic"}

response = requests.post(BASE + "userlog/1004", args) #test post
print("Test post: ", response.json())

response = requests.post(BASE + "userlog/1001", args) #test abort existing id
print("Test post existing id: ", response.json())

response = requests.delete(BASE + "userlog/1001") #test delete
print("Test delete: ", response.json())

response = requests.delete(BASE + "userlog/1007") #test abort existing id
print("Test delete invalid id: ", response.json())




