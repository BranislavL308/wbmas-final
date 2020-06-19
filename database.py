from serial import Serial
from pymongo import MongoClient
from json import loads,dumps

client = MongoClient()

db = client['baza']
collection = db.kolekcija

s = Serial('COM8')
while(1):
    result = ''
    a = s.read().decode()
    while a!='\n':
        result+=a
        a = s.read().decode()
        
    try:
        collection.insert_one(loads(result))
    except:
        pass