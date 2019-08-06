from pymongo import MongoClient
My_Client = MongoClient('mongodb://localhost:27017/')
db = My_Client.mulevaji
collection = db.aaditya
data = {
    "name": "aaditya",
    "last_name": "muleva",
    "grade": 25,
    "institute": "ips academy"
}
# to insert any data
# send = collection.insert_one(data)
# print("result sent: {} ".format(data))

# find any data
# send1 = db.aaditya.find_one({"grade": 25})
# for i in send1:
#     print("key '{}' : value '{}'".format(i,send1[i]))
# print("="*40)

# to update data
update = db.aaditya.update({"grade": 25}, {"$set":{"grade":"28"}})
#print ("updated 2.0 :",update)

# to delete data
delete = db.aaditya.remove({"institute": "ips academy"})
print("deleted :", delete)
