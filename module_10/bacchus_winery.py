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
cursor = db.cursor()

cursor.execute("CREATE TABLE employees (employee_id INT NOT NULL AUTO_INCREMENT, name VARCHAR(75), department VARCHAR(75), quarterly_hours INT, primary key(employee_id))")
cursor.execute("CREATE TABLE suppliers (supplier_id INT NOT NULL AUTO_INCREMENT, name VARCHAR(75), supplies VARCHAR(75), last_delivery VARCHAR(75), primary key(supplier_id))")
cursor.execute("CREATE TABLE distributors (distributor_id INT NOT NULL AUTO_INCREMENT, name VARCHAR(75), wine VARCHAR(75), tracking_id INT NOT NULL, primary key (distributor_id))")

db.close()