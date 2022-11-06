#importing necessary Package
import pymongo
import json

myclient=pymongo.MongoClient("mongodb://127.0.0.1:27017/")
mydb=myclient["student_DB"]
mycol=mydb["students_record"]
insert=mycol.insert_one(Data)
total_avg=mydb.total_avg
Avgrage_Candidates=mydb.Avgrage_Candidates
fail=mydb.fail
passed=mydb.passed


#Find the student name who scored maximum scores in all (exam, quiz and homework)?

data= mycol.aggregate([
    {"$unwind":"$scores"},
    {"$group":{"_id":"$_id","name":{"$first":"$name"},"Total":{"$sum":"$scores.score"}}},
    {"$sort":{"Total":-1}},
    {"$limit":1}
    ])
    
for i in data:
    print(i)
    


#Find students who scored below average in the exam and pass mark is 40%

query={'scores.type':'exam','scores.score':{'$gt':40,'$lt':60}}

data= mycol.aggregate([
    {'$unwind':'$scores'},
    {"$match":query}
    ])
    
for i in data:
    print(i)



#Find students who scored below pass mark and assigned them as fail, and above pass mark as pass in all the categories.

data=mycol.aggregate(
[ {"$set": 
   {"scores": 
     {"$arrayToObject": 
       [{"$map": 
           {"input": "$scores",
            "as": "s",
            "in": {"k": "$$s.type", "v": "$$s.score"}}}]}}},
 {"$project":
  {
     "_id":1,
     "name":1,
     "result":{
            "$cond":
                    {"if": {"$and" : [{"$gte": ["$scores.exam", 40]}, {"$gte": ["$scores.quiz", 40]}, {"$gte": [ "$scores.homework", 40]}]
                            },
                    "then" :"pass",
                    "else":"fail"
                    }
               }
  }
}
  ])
    
for i in data:
    print(i)
    
    
    
#Find the total and average of the exam, quiz and homework and store them in a separate collection

data=mycol.aggregate([
    {"$unwind":"$scores"},
    {"$group":
     {
         "_id":"$_id",
        "name":{"$first":"$name"}
      ,
     "Total":{"$sum":"$scores.score"},
      "Average":{"$avg":"$scores.score"}
      }
     },
     {"$sort":{"_id":1}}
     
     ])

data1=[]
for i in data:
  data1.append(i)
  print(i)

total_avg.insert_many(data1)



#Create a new collection which consists of students who scored below average and above 40% in all the categories.

data=mycol.aggregate(
[{"$match": 
   {"$expr": 
     {"$and": 
       [{"$gt": [{"$min": "$scores.score"}, 40]},
         {"$lt": [{"$max": "$scores.score"}, 70]}
        ]
      }
    }
  }])

Data1= []
for i in data:
  Data1.append(i)
  print(i)
  
Avgrage_Candidates.insert_many(Data1)



#Create a new collection which consists of students who scored below the fail mark in all the categories.

query={}
data=mycol.aggregate(
[{"$match": 
   {"$expr": 
     
       {"$lt": [{"$max": "$scores.score"}, 40]}
      
    }
  }])

fail_student = []
for i in data:
  faila.append(i)
  print(i)
  
fail.insert_many(fail_student)




#Create a new collection which consists of students who scored above pass mark in all the categories.

query={}
data=mycol.aggregate(
[{"$match": 
   {"$expr": 
     
       {"$gt": [{"$max": "$scores.score"}, 40]}
      
    }
  }])

passed1 = []
for i in data:
  passed1.append(i)
  print(i)
  
passed.insert_many(passed1)

