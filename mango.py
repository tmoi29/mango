from pymongo import MongoClient
c = MongoClient("lisa.stuy.edu", 27017)

db = c.test
col = db.restaurants


def get_borough(borough = "Queens"):
    cursor = col.find({"borough":borough})
    
    print cursor
    print "print cursor works"
    
    for each in cursor:
        print each

def get_zip(zip_code = "10282"):
    cursor = col.find({"address"."zipcode":zip_code})
    
    print cursor
    print "print cursor works"
    
    for each in cursor:
        print each

get_zip()
