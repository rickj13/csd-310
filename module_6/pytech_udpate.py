# Rick Jansen
# CYBR 410
# Module 6.2 Assignment: PyTech: Updating Documents
# July 9, 2023

#import MongoClient
from pymongo import MongoClient
#connect MongoDB url
url = "mongodb+srv://admin:admin@cluster0.mnsjngr.mongodb.net/?retryWrites=true&w=majority";
#connect MongoClient using variable url
client = MongoClient(url)
#assign db variable to pytech using variable client
db = client.pytech
#collect student data
students = db.students
#find students in list
student_list = students.find({})

#update student last name to Oakenshield II
result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Oakenshield II"}})
thorin = students.find_one({"student_id": "1007"})

#output all students' ID, first, and last name
print(" -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in student_list:
    print(" Student ID: " + doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")

print()

#output updated student
print(" -- DISPLAYING STUDENT DOCUMENT 1007 --")
print(" Student ID: " + thorin["student_id"] + "\n First Name: " + thorin["first_name"] + "\n Last Name: " + thorin["last_name"])

print()
print()
print()
print(" End of program, press any key to continue...█")
