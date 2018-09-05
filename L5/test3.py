from pymongo import MongoClient

connection = MongoClient('localhost', 27017)

db = connection.test

result = db.grades.aggregate([
    {
        '$unwind': "$scores"
    },
    {
        '$match': {
            '$or':
                [
                    {'scores.type': "exam"},
                    {'scores.type': "homework"}
                ]
        }
    },
    {
        '$group': {
            '_id': {'student': '$student_id', 'class': '$class_id'},
            'total': {'$avg': "$scores.score"}
        }
    },
    {
        '$group': {
            '_id': '$_id.class',
            'total_res': {'$avg': "$total"}
        }
    }
])

test = db.grades.find()

if __name__ == '__main__':
    for i in result:
        print(i)

