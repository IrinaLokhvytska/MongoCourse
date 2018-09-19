from pymongo import MongoClient

connection = MongoClient('localhost', 27017)

db = connection.enron
collection = db.messages

result = collection.aggregate([
    {
        '$unwind': '$headers.To'
    },
    {
        '$group': {
            '_id': '$_id',
            'from': {'$first': '$headers.From'},
            'to': {'$addToSet': '$headers.To'}
        }
    },
    {
        '$unwind': '$to'
    },
    {
        '$group': {'_id': {'From': '$from', 'To': '$to'}, 'total': {'$sum': 1}}
    },
    {'$sort': {'total': -1}},
    {'$limit': 1}
])

if __name__ == '__main__':
    for i in result:
        print(i)
