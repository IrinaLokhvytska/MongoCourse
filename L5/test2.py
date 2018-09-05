from pymongo import MongoClient

connection = MongoClient('localhost', 27017)

db = connection.test

result = db.zips.aggregate([
    {
        '$match': {
            '$or':
                [
                    {'state': "CA"},
                    {'state': "NY"}
                ]
        }
    },
    {
        '$match': {
            'pop': {'$gt': 25000}
        }
    },
    {
        '$group': {
            '_id': '$state',
            'total': {'$avg': "$pop"}
        }
    }
])

test = db.zips.find()

if __name__ == '__main__':
    for i in result:
        print(i)

