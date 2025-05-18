import os
from dotenv import load_dotenv
from pymongo import MongoClient


load_dotenv()


MONGO_HOST = os.getenv("MONGO_HOST")
MONGO_PORT = int(os.getenv("MONGO_PORT"))
MONGO_USER = os.getenv("MONGO_USER")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")


client = MongoClient(
    host=MONGO_HOST,
    port=MONGO_PORT,
    username=MONGO_USER,
    password=MONGO_PASSWORD,
    authSource="admin"
)

db = client["sunjerry_test"]
collection = db["environment"]

def get_mongo_data_by_layer(layer_key):
    return list(collection.find({"Layer": layer_key}))
