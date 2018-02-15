from pymongo import MongoClient
c = MongoClient("lisa.stuy.edu", 27017)

db = c.test
col = db.restaurants


def get_borough(borough = "Queens"):
    cursor = col.find({"borough":borough})
    for each in cursor:
        print each

def get_zip(zip_code = "11368"):
    cursor = col.find({"address.zipcode":zip_code})
    
    for each in cursor:
        print each

def get_zip_grade(zip_code = "11368", grade = "A"):
    cursor = col.find({"grades.grade":grade}, {"address.zipcode":zip_code})
    for each in cursor:
        print each

def get_zip_score(zip_code = "11368", score = 10):
    cursor = col.find({"grades.score":{ "$lt" : score }}, {"address.zipcode":zip_code})
    for each in cursor:
        print each

get_zip_score()