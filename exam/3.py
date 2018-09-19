from pymongo import MongoClient

connection = MongoClient('localhost', 27017)

db = connection.enron
collection = db.messages

collection.update_many(
    {"headers.Message-ID": "<8147308.1075851042335.JavaMail.evans@thyme>"},
    {'$push': {"headers.To": "mrpotatohead@mongodb.com"}}
)


if __name__ == '__main__':
    pass
