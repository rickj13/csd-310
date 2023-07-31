# Rick Jansen
# CYBR 410
# Module 6.3 Assignment: PyTech: Deleting Documents
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

#output all students' ID, first, and last name
print(" -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in student_list:
    print(" Student ID: " + doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")

print()

#new student
new_student = {
  "student_id": "1010",
  "first_name": "John",
  "last_name": "Doe"
}

#insert new student
new_student_id = students.insert_one(new_student).inserted_id

#inserted new student
print(" -- INSERT STATEMENTS --")
print(" Inserted student record into the students collection with document_id " + str(new_student_id))

print()

#call the new student
student_new_student = students.find_one({"student_id": "1010"})

#display the new student
print(" -- DISPLAYING STUDENT TEST DOC --")
print(" Student ID: " + student_new_student["student_id"])
print(" First Name: " + student_new_student["first_name"])
print(" Last Name: " + student_new_student["last_name"])

print()

#delete the new student
delete_student_new_student = students.delete_one({"student_id": "1010"})

#find updated students in list
updated_student_list = students.find({})

print()

#output all students' ID, first, and last name
print(" -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in updated_student_list:
    print(" Student ID: " + doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")

print()
print()
print(" End of program, press any key to continue...")
