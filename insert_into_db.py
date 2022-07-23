#sample creation
import pymongo
client = pymongo.MongoClient("mongodb+srv://system:<password>@cluster0.0rtf2.mongodb.net/?retryWrites=true&w=majority")
#<password> use your password
db = client.test
d = {
    "name":"Shabarish",
    "email" : "shabari@gmail.com",
    "surname" : "meda"
}
db1 = client['mongotest']  # database name if exists uses it else create new one
coll = db1['test']  # like table name if exists uses it else create new one
coll.insert_one(d)
