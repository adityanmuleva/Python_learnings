from pymongo import MongoClient
import datetime
Client_random = MongoClient('mongodb://localhost:27017/')
db = Client_random["Hospital"]
coll = db.myname
data = {
    "patientName": "xyz",
    "patientAge": 90,
    "disease": "viral",
    "date of admission": datetime.datetime.now()
}
run = coll.insert_one(data)
run1 = db.myname.find({"patientName": "xyz"})
for doc in run1:
    print ("Begin")
    for x in doc:
        print (x, " value", doc[x])
    print ("end")
#print("inserted successfully : {}".format(run1))
