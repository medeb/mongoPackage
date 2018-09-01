import subprocess
import pymongo
from pymongo import MongoClient
from bson.json_util import loads
from bson import json_util
from bson.json_util import dumps

class connection:
    try:
        client =  MongoClient('localhost',27017)
        print("Connected To MongoDB!")
        print("****")*15
    except:
        print("Couldn't connect to mongodb")


    #Database
    print("Databases : ")
    docs = client.database_names()
    for i in docs:
        print("   " + i)

    iChecker = 0
    while(True):
        try:
            db_name = raw_input("Use existing Database or Create a new one : ")
            db = client[db_name]
            break
        except:
            print("Database name can't be empty! Try Again")
            iChecker = iChecker + 1
            if iChecker < 3:
                continue
            else:
                break


    #workon collection
    try:
        cols = db.collection_names()
        print("****")*15
        print("Collections : ")
        for i in cols:
            print("   " + i)
    except NameError:
        print("****")*15
        print("Database name not defined!")
        exit()

    iChecker = 0
    while(True):
        try:
            col_name = raw_input("Enter Collection name : ")
            col = db[col_name]
            print("All Ready Let's Continue \n")
            break
        except:
            print("Collection name can't be empty! Try Again")
            iChecker = iChecker + 1
            if iChecker < 3:
                continue
            else:
                break
