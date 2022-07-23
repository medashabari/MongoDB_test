import pymongo
client = pymongo.MongoClient("mongodb+srv://system:system@cluster0.0rtf2.mongodb.net/?retryWrites=true&w=majority")
db = client.test

data ={
    "name" : "shabarish",
    "mail_id" : "shabari@gmail.com",
    "subject" : ["DataScience","Big Data","Data analytics"]
}  # one document

database = client['myinfo'] #create a database.This is database creation
collection = database['test'] # creating a collection. IN sql we call table in mongoDB we call collection
collection.insert_one(data)