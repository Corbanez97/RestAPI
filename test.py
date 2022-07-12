from urllib import response
import requests

BASE = "http://127.0.0.1:5000/" ##Running on FlaskAPI Server

response = requests.get(BASE + "userlog/1001") #test get
print(response.json())

response = requests.get(BASE + "userlog/1004") #test abort invalid id
print(response.json())

response = requests.post(BASE + "userlog/1001") #test post
print(response.json())

#test put
response = requests.put(BASE + "userlog/1004", {"name": "Paola", "age": 26, "job": "Medic"})
print(response.json())

#test abort existing id
response = requests.put(BASE + "userlog/1001", {"name": "Paola", "age": 26, "job": "Medic"})
print(response.json())

