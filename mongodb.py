import pymongo
client = pymongo.MongoClient("mongodb+srv://KajanT:Kajan123@cluster0.ylfenqf.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name": "sudhanshu",
    "email":"sudh@gmail.com"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)

