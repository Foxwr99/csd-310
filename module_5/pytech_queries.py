"""Wendy Rodriguez
June 19, 2022
Module 5.3 Assignment
"""

from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.q1zeowl.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
students = client.pytech.get_collection("students")

print("--DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
docs = students.find()
for doc in docs:
    print("\nStudent ID: ", doc["student_Id"], "\nFirst Name: ", doc["first_name"], "\nLast Name: ", doc["last_name"])

print("\n-- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
doc = students.find_one({"student_Id": "1007"})
print("\nStudent ID: ", doc["student_Id"], "\nFirst Name: ", doc["first_name"], "\nLast Name: ", doc["last_name"])

print("\nEnd of program, press any key to continue...")