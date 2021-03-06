import mysql.connector
# Connect to the database
config = {
    "user" : "winery_user",
    "password": "wendy1981",
    "host": "127.0.0.1",
    "database": "winery",
    "raise_on_warnings": True
}
db = mysql.connector.connect(**config)

#Create cursor to obtain information from the distributors table

cursor = db.cursor()

# Add columns "expected_sales" and "actual_sales" to distributors table
cursor.execute('ALTER table distributors add column expected_sales VARCHAR(75) after wine')
cursor.execute('ALTER table distributors add column actual_sales VARCHAR(75) after expected_sales')

# Insert data into the inserted columns
cursor.execute('UPDATE distributors SET expected_sales = "500"')
cursor.execute('UPDATE distributors SET actual_sales = "490" WHERE distributor_id = 1001')
cursor.execute('UPDATE distributors SET actual_sales = "85" WHERE distributor_id = 1002')
cursor.execute('UPDATE distributors SET actual_sales = "450" WHERE distributor_id = 1003')
cursor.execute('UPDATE distributors SET actual_sales = "100" WHERE distributor_id = 1004')
cursor.execute('UPDATE distributors SET actual_sales = "500" WHERE distributor_id = 1005')
cursor.execute('UPDATE distributors SET actual_sales = "600" WHERE distributor_id = 1006')
db.commit()

