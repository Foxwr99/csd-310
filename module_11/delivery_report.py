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

cursor.execute('SELECT name, expected_delivery, actual_delivery FROM suppliers')

suppliers = cursor.fetchall()

print("\n ----- 6 MONTH SUPPLIER DELIVERY REPORT -----")

for supplier in suppliers:
    print("\nSupplier Name: {}".format(supplier[0]), "\nExpected Delivery Date: {}".format(supplier[1]), "\nActual Delivery Date: {}".format(supplier[2]))
print()
print()
print("Press any key to continue...")
print()