import pymongo

# connecting to momgoDB
client = pymongo.MongoClient("mongodb+srv://system:system@cluster0.0rtf2.mongodb.net/?retryWrites=true&w=majority")
db = client.test

data =  [
        {
            "item": "canvas",
            "qty": 100,
            "size": {"h": 28, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "journal",
            "qty": 25,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mat",
            "qty": 85,
            "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mousepad",
            "qty": 25,
            "size": {"h": 19, "w": 22.85, "uom": "cm"},
            "status": "P",
        },
        {
            "item": "notebook",
            "qty": 50,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "P",
        },
        {
            "item": "paper",
            "qty": 100,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "D",
        },
        {
            "item": "planner",
            "qty": 75,
            "size": {"h": 22.85, "w": 30, "uom": "cm"},
            "status": "D",
        },
        {
            "item": "postcard",
            "qty": 45,
            "size": {"h": 10, "w": 15.25, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketchbook",
            "qty": 80,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketch pad",
            "qty": 95,
            "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
            "status": "A",
        },
    ]
# $ is to be used for condition
database = client['inventory']  # connecting to database
collection = database['table']  # accessing the collection inside database
# collection.insert_many(data)  # inseting multiple data
# d=collection.find()  # retrieving the data
# d=collection.find({'status':'A'})  # selecting the data where status = A
# d = collection.find({'status':{'$in':['A','P']}}) # selecting the data where status is = A or P
# d = collection.find({'status':{'$gt':'C'}}) # selecting the data where status greater than C
# d = collection.find({'qty':{'$gte':100}}) # selecting the data where qty greater than eql to 100
# d = collection.find({'qty':{'$lt':100}})  # selecting the data where qty less than 100
# d = collection.find({'qty':{'$gt':50},'qty':{'$lt':100}}) # and condition--> selecting the data where qty > 50 and qty<100
# d = collection.find({'item':'sketch pad','qty':95}) # selecting the data where item = sketch pad and qty = 95
# d= collection.find({'item':'sketch pad','qty':{"$gte":100}}) # selecting the data where item = sketch pad and qty >= 100
# d = collection.find({'$or':[{'item':'sketch pad'},{'qty':{"$gte":75}}]})  # or condtion --> selecting the data where item = sketch pad or qty >= 75
d = collection.find({'status':{'$gt':'C'},'$or':[{'item':'sketch pad'},{'qty':{"$gte":75}}]}) # selecting the data where (status >) C and (item ='sketch pad' or qty >= 75)

# update
# collection.update_one({'item':'canvas'},{'$set':{'item':'Shabu'}}) $ updating the item canvas to shabu
# collection.update_one({'item': 'canvas'} , {'$set':{'item': 'sudhanshu'} })
# d= collection.find({'item':'Shabu'})

# delete
# collection.delete_one({'item': 'Shabu'}) # deleting the item shabu
# d = collection.find({'item':'Shabu'})
for i in d:
    print(i)