from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv, find_dotenv
import os
import pprint

load_dotenv(find_dotenv())
# Get the password from environment variable
password = os.environ.get('MONGODB_PASSWORD')

uri = "mongodb+srv://zack-learner:<password>@cluster0.pskipq1.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)