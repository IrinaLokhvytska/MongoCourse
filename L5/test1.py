from pymongo import MongoClient

connection = MongoClient('localhost', 27017)

db = connection.blog

result = db.posts.aggregate([
    {
        '$unwind': "$comments"
    },
    {
        '$group': {
            '_id': '$comments.author',
            "count": {"$sum": 1}
        }
    }
])

test = db.posts.find_one()
answer = {'author': '', 'num': 0}
if __name__ == '__main__':
    for i in result:
        if i['count'] > answer['num']:
            answer['num'] = i['count']
            answer['author'] = i['_id']

    print(answer)
