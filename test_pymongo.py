# connect to the MongoDB server with username and password
import pymongo
import pprint
from bson.objectid import ObjectId

username = 'nexa'
password = 'nexa2023alexzack'
host = '10.138.0.7'
ports = [27117, 27118]

#mongo_url = f"mongodb://{username}:{password}@{host}:{ports[0]},{host}:{ports[1]}/?authMechanism=DEFAULT"
#client = pymongo.MongoClient(mongo_url)

mongo_url = "mongodb+srv://nexa2023:F4scqyirRIP3B2Rq@nexa-test.xcioe22.mongodb.net/test"
client = pymongo.MongoClient(mongo_url)
test_db = client['test']
collection = test_db['experiment']
printer = pprint.PrettyPrinter(indent=4)
# list all current db
dbs = client.list_database_names()
print(dbs)

# insert document (row)
def insert_test_doc():
    collection = test_db['experiment']
    test_document= {
        "name": "zack" ,
        "type": "test"
    }
    inserted_id = collection.insert_one(test_document).inserted_id # insert_many : for a list of dict
    return inserted_id

# insert x documents (x rows)
def insert_test_docs(test_db):
    collection = test_db['experiment']
    test_documents= [{
        "name": "alex" ,
        "type": "prioduction"
    },
    {
        "name": "alex" ,
        "type": "test"
    },
    {
        "name": "zack" ,
        "type": "production"
    }]
    inserted_ids = collection.insert_many(test_documents).inserted_ids # insert_many : for a list of dict
    return inserted_ids

#print all history
def find_all_people(collections):
    people = collections.find() # write a query
    #print(people) # <pymongo.cursor.Cursor object at 0x7f3e4a994e90>
    #print(list(people)) # print cursor
    # for person in people:
    #     pprint.pprint(person)

def find_with_query(collections, query):
    people = collections.find(query) # use find_one() if we only need 1st result
    for person in people:
        pprint.pprint(person)

def find_with_id(collections, person_id):
    _id = ObjectId(person_id) # a special object in BSON
    people = collections.find({"_id":_id}) # use find_one() if we only need 1st result
    for person in people:
        pprint.pprint(person)

def update_person_by_id(collections, person_id):
    _id = ObjectId(person_id) # a special object in BSON
    all_updates = {
        "$set": {"new_field": True},
        "$rename": {"name":"Sundar", "type":"experiment"}
    }
    collections.update_one({"_id": _id}, all_updates)

if __name__ == "__main__":
    # collections (table)
    test_db = client['test']
    test_collections = test_db.list_collection_names()
    print(test_collections) # ['experiment']

    # inserted_id = insert_test_doc(test_db)
    # print("zack debug: ", inserted_id)
    # inserted_ids = insert_test_docs(test_db)
    # print("zack debug: ", inserted_ids)
    # find_all_people(collection)

    query = {"name": "zack"}
    find_with_query(collection, query)

    person_id = "64542d6d0dcd9972ea3423a3"
    find_with_id(collection, person_id)

    update_person_by_id(collection, '64542d6d0dcd9972ea3423a3')
