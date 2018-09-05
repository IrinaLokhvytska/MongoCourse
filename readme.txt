* Running project with Python 2:
py -2 -m pip install pymongo
py -2 blog.py
py -2 validate.py

* Lesson 5
mongoimport --drop -d blog -c posts posts.json
mongoimport --drop -d test -c zips small_zips.json
mongoimport --drop -d test -c grades grades.json
mongoimport --drop -d test -c zips zips.json
