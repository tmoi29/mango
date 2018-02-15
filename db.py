"""
Yuanchu Liu and Tiffany Moi
SoftDev2 pd7
K04 -- Mi only nyam ital food, mon!
2018-02-15
"""

from pymongo import MongoClient
import urllib2, json


"""
SETUP

def load_json():
    url = "http://api.nobelprize.org/v1/laureate.json"
    uResp = urllib2.urlopen(url)
    info = json.loads(uResp.read())
    return info

c = MongoClient("lisa.stuy.edu", 27017)

db = c["mango"]

json = load_json()

for laureate in json["laureates"]:
    db.laureates.insert(laureate)"""
    
c = MongoClient("lisa.stuy.edu", 27017)  
db = c.mango
col = db.laureates

#Finds Laureates born in a given country
def search_birthCountry(country = "USA"):
    cursor = col.find({"bornCountry":country})
    for each in cursor:
        print each
#search_birthCountry()

#Finds Laureates who died in a given country
def search_deathCountry(country = "USA"):
    cursor = col.find({"diedCountry":country})
    for each in cursor:
        print each
#search_deathCountry()

def search_birth_category(country = "USA", cat = "physics"):
    cursor = col.find({"diedCountry":country, "prizes.category": cat})
    for each in cursor:
        print each
search_birth_category()


#Finds Laureates who recieved award under a given age

def search_age(age = 60):
    cursor = col.find({"borough":borough})
    for each in cursor:
        print each
