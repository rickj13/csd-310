# Rick Jansen
# CYBR 410
# Module 6.2 Assignment: PyTech: Updating Documents
# July 9, 2023

from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.mnsjngr.mongodb.net/?retryWrites=true&w=majority";
client = MongoClient(url)
db = client.pytech
students = db.students
student_list = students.find({})

result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Oakenshield II"}})
thorin = students.find_one({"student_id": "1007"})

print(" -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in student_list:
    print(" Student ID: " + doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")

print()

print(" -- DISPLAYING STUDENT DOCUMENT 1007 --")
print(" Student ID: " + thorin["student_id"] + "\n First Name: " + thorin["first_name"] + "\n Last Name: " + thorin["last_name"])

print()
print()
print()
print(" End of program, press any key to continue...█")