<<<<<<< HEAD
"""Wendy Rodriguez
June 23, 2022
Module 6.2 Assignment"""


from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.q1zeowl.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
students = client.pytech.get_collection("students")

#Print results of find() query

print("--DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
docs = students.find()
for doc in docs:
    print("\nStudent ID: ", doc["student_Id"], "\nFirst Name: ", doc["first_name"], "\nLast Name: ", doc["last_name"])
print()

#Update the last name for Student ID 1007 to De La Ree

result = students.update_one({"student_Id": "1007"}, {"$set": {"last_name": "De la Ree"} })

#Print result of updated student

print("-- DISPLAYING UPDATED STUDENT DOCUMENT FROM find_one() QUERY --")

updated_student = students.find_one({"student_Id": "1007"})
print("\nStudent ID: ", updated_student["student_Id"], "\nFirst Name: ", updated_student["first_name"], 
"\nLast Name: ", updated_student["last_name"])
    
print()
print()
=======
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.q1zeowl.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
students = client.pytech.get_collection("students")

#Print results of find() query

print("--DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
docs = students.find()
for doc in docs:
    print("\nStudent ID: ", doc["student_Id"], "\nFirst Name: ", doc["first_name"], "\nLast Name: ", doc["last_name"])
print()

#Update the last name for Student ID 1007 to De La Ree

result = students.update_one({"student_Id": "1007"}, {"$set": {"last_name": "De la Ree"} })

#Print result of updated student

print("-- DISPLAYING UPDATED STUDENT DOCUMENT FROM find_one() QUERY --")

updated_student = students.find_one({"student_Id": "1007"})
print("\nStudent ID: ", updated_student["student_Id"], "\nFirst Name: ", updated_student["first_name"], 
"\nLast Name: ", updated_student["last_name"])
    
print()
print()
>>>>>>> 60be9b99ecf90ebb0de8413dd57cce24572f0dd2
print("End of program, press any key to continue...")