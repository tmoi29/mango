"""
Yuanchu Liu and Tiffany Moi
SoftDev2 pd7
K04 -- Mi only nyam ital food, mon!
2018-02-15
"""

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
    cursor = col.find({"grades.grade":grade, "address.zipcode":zip_code})
    for each in cursor:
        print each

def get_zip_score(zip_code = "11368", score = 10):
    cursor = col.find({"grades.score":{ "$lt" : score }, "address.zipcode":zip_code})
    for each in cursor:
        print each

def restaurant_search(name = "null", zip_code = "null", cuisine = "null"):
    """
    TODO
    Expand to a full search, make parameters optional
        Challenges:
            eval("col.find({ <param_in_string_form_here> })") doesn't recognize col as MongoClient("lisa.stuy.edu",27017).test.restaurants (does not keep track of vars)
                (also eval() is bad)
            The closest thing to a wildcard query is <param>:{$exist = true}, but that isn't a string and so cannot be easily replaced in col.find() by a string
        Result:
            Sad function here with unnecessary default args and filtering
    """
    if name != "null":
        name_search_param = name
    if zip_code != "null":
        zip_search_param = zip_code
    if cuisine != "null":
        cuisine_search_param = cuisine

    cursor = col.find({"name":name_search_param, "address.zipcode":zip_search_param, "cuisine":cuisine_search_param})
    for each in cursor:
        print each

restaurant_search("Jing Way Food","11220","Other")
