from pymongo import MongoClient

connection = MongoClient('localhost', 27017)

db = connection.test

result = db.zips.aggregate([
    {
        '$group': {
            '_id': "$city",
            'total': {'$sum': "$pop"}
        }
    }
])

test = db.zips.find()
total = 0

if __name__ == '__main__':
    for i in result:
        if i['_id'][0] in ("B", "D", "O", "G", "N", "M"):
            total += i['total']
    print(total)

