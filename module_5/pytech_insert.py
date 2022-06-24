"""Wendy Rodriguez
June 19, 2022
Module 5.3 Assignment
"""

from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.q1zeowl.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
students = client.pytech.get_collection("students")

# Inserting documents to database
wendy = {"student_Id": "1007", 
    "first_name": "Wendy", 
    "last_name": "Rodriguez"}
lorna = {"student_Id": "1008", 
    "first_name": "Lorna", 
    "last_name": "Doone"}
tess = {"student_Id": "1009", 
    "first_name": "Tess", 
    "last_name": "D'Urbervilles"}

wendy_student_Id = students.insert_one(wendy).inserted_id
lorna_student_Id = students.insert_one(lorna).inserted_id
tess_student_Id = students.insert_one(tess).inserted_id

# Print the insert statements
print("-- INSERT STATEMENTS --")
print("Inserted student record Wendy Rodriguez into the students collection with document_id ", wendy_student_Id)
print("Inserted student record Lorna Doone into the students collection with document_id ", lorna_student_Id)
print("Inserted student record Tess D'Urbervilles into the students collection with document_id ", tess_student_Id)

# Print End of Program
print("\nEnd of program, press any key to exit...")