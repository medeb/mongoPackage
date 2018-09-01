import subprocess
import pymongo
import json
from pymongo import MongoClient
from bson.json_util import loads
from bson import json_util
from bson.json_util import dumps
from model import connection as con


def read():
    """Used to read documents of a collection."""

    doc = con.col.find()
    for i in doc:
        print(i)

def find():
    """Used to find documents."""

    id = raw_input("Enter unique id : ")
    doc = con.col.find({"_id":id})
    for i in doc:
        print(i)

def find_element(id):
    """Returns document if exists"""

    return(con.col.find({"_id":id}))

def export():
    """Used to export data to a new json file using."""

    subprocess.call(["mongoexport", "--db",con.db_name,"-c",con.col_name,"--out","output.json"])
    print("Export Completed!\nCheck output.json file")

def insert():
    """Used to insert Data from a json file to database."""
    try:
        with open('data.json') as jfile:
            json_decoded=json.load(jfile)

        if '_id' not in json_decoded:
            id = raw_input("Enter unique id : ")
            json_decoded["_id"]=id

            try:
                con.col.insert_one(json_decoded)
            except:
                print("Duplicate key! Key has to be unique! \n Try again")

    except IOError:
        print("Unable to open the file. Check again!")

def update():
    """Used to update document."""

    id = raw_input("Enter unique id : ")
    doc = find_element(id)
    
    while(True):    
        key = raw_input("Enter key : ")
        if not key:
            break
        else:
            key_value = raw_input("Enter value : ")
            con.col.update_one({"_id": id},{"$set":{key : key_value}},upsert=False)
            print("Updated successfully! \n")

def delete(x):
    """Used to delete the collections and documents."""

    if x == "1":
        id = raw_input("Enter id : ")
        try:
            con.col.delete_many({"_id":id})
            print("Deleted successfully!")
        except:
            print("Doesn't exists!")

    elif x == "2":
        try:
            con.col.drop()
            print("Deleted successfully!")
        except:
            print("Error in dropping collection!")



print("Operations : ")

while(True):

    print("\n1.INSERT 2.EXPORT 3.READ 4.FIND 5.UPDATE 6.DELETE\n ")
    case_statement = raw_input("Enter : ")

    if case_statement == "1":
        insert()
    elif case_statement == "2":
        export()
    elif case_statement == "3":
        read()
    elif case_statement == "4":
       find()
    elif case_statement == "5":
        update()
    elif case_statement == "6":
        d = raw_input("DELETE 1.DOCUMENT 2.COLLECTION : ")
        delete(d)
    else:
        exit()


   