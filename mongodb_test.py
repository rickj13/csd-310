# Rick Jansen
# CYBR 410
# Module 5.2 Assignment: PyTech: Collection Creation
# July 2, 2023

from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.mnsjngr.mongodb.net/?retryWrites=true&w=majority";
client = MongoClient(url)
db = client.pytech
print(" -- Pytech COllection List -- ")
print(db.list_collection_names())
print()
print()
print("  End of program, press any key to exit... █")
