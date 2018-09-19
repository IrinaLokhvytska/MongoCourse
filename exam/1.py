from pymongo import MongoClient

connection = MongoClient('localhost', 27017)

db = connection.enron
collection = db.messages

test = collection.find(
    {"headers.From": "andrew.fastow@enron.com"}
)

if __name__ == '__main__':
    for i in test:
        print(i["headers"])
