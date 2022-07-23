import pymongo
client = pymongo.MongoClient("mongodb+srv://system:system@cluster0.0rtf2.mongodb.net/?retryWrites=true&w=majority")
db = client.test

database = client['myinfo']
collection = database['test']
"""records = collection.find()
for i in records:
    print(i)"""

#data = collection.find({"companyName":"iNeuron"})
#gt=greater than gte=greater than equal like lt, lte
data = collection.find({'courseOffered':{"$gt":"E"}})
for i in data:
    print(i)