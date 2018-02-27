"""
Yuanchu Liu and Tiffany Moi
SoftDev2 pd7
K05 -- Import/Export Bank
2018-02-26
"""

from pymongo import MongoClient
import urllib2, json


"""
This database is a list of all Nobel Prize laureates and their information, including the laureate's full name, date and place of birth and death, award, its year, category, and reason for receiving the award.

name             : Laureate

source           : nobelprize.org

url              : http://api.nobelprize.org/v1/laureate.json

import mechanism : The import mechanism takes advantage of the json format of the original dataset, especially the fact that every entry (every laureate) is formatted as a doc. Each laureate is inserted "as is" into the database from the .json dataset.

"""

"""
SETUP CODE
ENABLE TO UPLOAD DATASET ONTO LISA.STUY.EDU

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
    
def get_col():
    c = MongoClient("lisa.stuy.edu", 27017)  
    db = c.mango
    col = db.laureates
    return col


#Finds Laureates born in a given country
def search_birthCountry(col, country = "USA"):
    cursor = col.find({"bornCountry":country})
    ret = []
    for each in cursor:
        ret.append(each)
    return ret
#search_birthCountry()

#Finds Laureates who died in a given country
def search_deathCountry(col, country = "USA"):
    cursor = col.find({"diedCountry":country})
    ret = []
    for each in cursor:
        ret.append(each)
    return ret
#search_deathCountry()

#Finds Laureates from a given country who won a prize in a given category
def search_category(col, cat = "physics"):
    cursor = col.find({"prizes.category": cat})
    ret = []
    for each in cursor:
        ret.append(each)
    return ret
#search_category()

#Finds Laureates that won a prize in a given year
def search_year_won(col, year = 2000):
    cursor = col.find({"prizes.year": str(year)})
    ret = []
    for each in cursor:
        ret.append(each)
    return ret
#search_year_won()

#Finds Laureates with a given name

def search_name(col, f_name = "Albert", surname= "Einstein"):
    cursor = []
    if (f_name == ""):
         cursor = col.find({"surname": surname})
    if (surname == ""):
        cursor = col.find({"firstname": f_name})
    if (f_name != "" and surname != ""):
        cursor = col.find({"$and":[{"surname": surname}, {"firstname": f_name}]})
    ret = []
    for each in cursor:
        ret.append(each)
    return ret
#search_name()

