import json
from pymongo import MongoClient
client=MongoClient('mongodb://127.0.0.1:27017')
db=client["task02_student"]
collections=db["student_data"]
data = open("C:/admin/Downloads/students.json")
student_data=json.load(data)
