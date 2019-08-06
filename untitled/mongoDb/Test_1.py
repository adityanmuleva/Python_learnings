from pymongo import MongoClient
client = MongoClient('mongodb://localhost:3001')
db = client.meteor
collection=db.getdatas
data = [{"name": "arpita",
			 "age":16
         },{
          "name": "aaditya",
			  "age": 20
		}]

result = collection.insert_many(data)
print("result inserted", result)
#print result