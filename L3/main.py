from pymongo import MongoClient
from collections import defaultdict

connection = MongoClient('localhost', 27017)

db = connection.school

scores = defaultdict(lambda: defaultdict(list))
for i in db.students.find({}):
    for e in i['scores']:
        scores[(i['_id'], i['name'])][e['type']].append(e['score'])

result = defaultdict(float)
for k, v in scores.items():
    for e in v:
        for t, s in v.items():
            if t == 'homework':
                result[k] += max(s)
            else:
                result[k] += s[0]


if __name__ == '__main__':
    for k, v in result.items():
        print(k, v)

