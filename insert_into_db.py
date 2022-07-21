import pymongo
client = pymongo.MongoClient("mongodb+srv://system:<password>@cluster0.0rtf2.mongodb.net/?retryWrites=true&w=majority")
#<password> use your password
db = client.test
d = {
    "name":"Shabarish",
    "email" : "shabari@gmail.com",
    "surname" : "meda"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)
