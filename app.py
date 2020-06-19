from flask import Flask,render_template,url_for,request,redirect, make_response
import random
import json
from time import time
from random import random
from flask import Flask, render_template, make_response
import pymongo




app = Flask(__name__)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["baza"]
mycol = mydb["kolekcija"]



@app.route('/', methods=["GET", "POST"])
def main():
    return render_template('index.html')


@app.route('/data', methods=["GET", "POST"])
def data():
 
    dataListT = []
    dataListT = dataListT[1:]
    for x in mycol.find({},{"Temperatura": 1, "_id": 0 }):
        for value in x.values():
            dataListT.append(value)
    dataListT = list(map(int, dataListT)) 
    Temperature = dataListT[-1]

    dataListP = []
    dataListP = dataListP[1:]
    for x in mycol.find({},{"Preasure": 1, "_id": 0 }):
        for value in x.values():
            dataListP.append(value)
    dataListP = list(map(int, dataListP))
    Preasure = dataListP[-1]

    dataListH = []
    dataListH = dataListH[1:]
    for x in mycol.find({},{"Humidity": 1, "_id": 0 }):
        for value in x.values():
            dataListH.append(value)
    dataListH = list(map(int, dataListH))
    Humidity = dataListH[-1]

    dataListU = []
    dataListU = dataListU[1:]
    for x in mycol.find({},{"UV": 1, "_id": 0 }):
        for value in x.values():
            dataListU.append(value)
    dataListU = list(map(int, dataListU))
    UlV = dataListU[-1]

    data = [time() * 1000, Temperature, Preasure, Humidity, UlV]
    response = make_response(json.dumps(data))

    response.content_type = 'application/json'

    return response


if __name__ == "__main__":
    app.run(debug=True)


