"""
Yuanchu Liu and Tiffany Moi
SoftDev2 pd7
K05 -- Import/Export Bank
2018-02-26
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
    db.laureates.insert(laureate)
    """
    
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

#Finds Laureates from a given country who won a prize in a given category
def search_birth_category(country = "USA", cat = "physics"):
    cursor = col.find({"diedCountry":country, "prizes.category": cat})
    for each in cursor:
        print each
#search_birth_category()

#Finds Laureates that won a prize in a given year
def search_year_won(year = 2000):
    cursor = col.find({"prizes.year": str(year)})
    for each in cursor:
        print each
#search_year_won()

#Finds Laureates with a given name

def search_name(name = "Albert Einstein"):
    surname = name.split(" ")[1]
    first = name.split(' ')[0]
    cursor = col.find({"$and":[{"surname": surname}, {"firstname": first}]})
    for each in cursor:
        print each
search_name()

