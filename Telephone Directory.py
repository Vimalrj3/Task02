import pymongo
client=pymongo.MongoClient('mongodb://127.0.0.1:27017')

#Create a database
db=client["task02"]

#Create a collection
collections=db.directory

#insert Records
record=([{"Name": "Suresh", "PhoneNo": 123456789, "Place": "Trichy"},
                         {"Name": "Ramesh", "PhoneNo": 987654321, "Place": "Chennai"},
                         {"Name": "Umesh", "PhoneNo": 321654987, "Place": "Madurai"},
                         {"Name": "Mahesh", "PhoneNo": 654321987, "Place": "Erode"},
                         {"Name": "Rakesh", "PhoneNo": 987321654, "Place": "Coimbatore"}])
collections.insert_many(record)
for data in collections.find():
    print(data)
    
    
# query to find records
collections.find()
for data in collections.find():
    print(data)

record=collections.find({"Place":{"$in":["Chennai","Madurai"]}})
for data in record:
    print(data)
    
    

#Modify the records
collections.update_many({"Name":"Ramesh"},{"$set":{"Name":"Ramesh Chandran"}})
for data in collections.find():
    print(data)
    

 #Delete the record
collections.delete_one({"Name":"Umesh"})
for data in collections.find():
    print(data)
    


    

    
    

