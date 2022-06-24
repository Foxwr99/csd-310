from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.q1zeowl.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
students = client.pytech.get_collection("students")

# Print results of find() query

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
docs = students.find()
for doc in docs:
    print("\nStudent ID: ", doc["student_Id"], "\nFirst Name: ", doc["first_name"], "\nLast Name: ", doc["last_name"])
print()

# Insert document for Student ID 1010

lizzie = {"student_Id": "1010",
    "first_name": "Elizabeth",
    "last_name": "Bennet"}

lizzie_student_Id = students.insert_one(lizzie).inserted_id

# Print inserted document statement

print("-- INSERT STATEMENTS --")
print("\nInserted student record 1010 into the students collection with document_id ", lizzie_student_Id)
print()

# Print results of find() query with inserted document

print("-- DISPLAYING NEW STUDENT LIST DOC --")
docs = students.find()
for doc in docs:
    print("\nStudent ID: ", doc["student_Id"], "\nFirst Name: ", doc["first_name"], "\nLast Name: ", doc["last_name"])
print()

# Delete document for Student ID 1010 with delete_one() method

students.delete_one({"student_Id": "1010"})

# Print results of find() query 

print("-- DELETED STUDENT ID: 1010 --")
docs = students.find()
for doc in docs:
    print("\nStudent ID: ", doc["student_Id"], "\nFirst Name: ", doc["first_name"], "\nLast Name: ", doc["last_name"])
print()
print()
print("End of program, press any key to continue...")