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
cursor.execute("INSERT INTO suppliers (supplier_id, name, supplies, expected_delivery, actual_delivery) VALUES ('21', 'Corks R Us', 'corks and bottles', '1 July 2022', '2 July 2022')")
cursor.execute("INSERT INTO suppliers (supplier_id, name, supplies, expected_delivery, actual_delivery) VALUES ('22', 'Printers and Stuff', 'labels and boxes', '15 June 2022', '20 June 2022')")
cursor.execute("INSERT INTO suppliers (supplier_id, name, supplies, expected_delivery, actual_delivery) VALUES ('23', 'Sampson Supplies', 'vats and tubing', '30 June 2022', '1 July 2022')")
db.commit()

cursor.execute("SELECT supplier_id, name, supplies, expected_delivery, actual_delivery FROM suppliers") 
supplierlist = cursor.fetchall()
for suppliers in supplierlist:
    print("\nSupplier ID: {}".format(suppliers[0]),

     "\nName: {}".format(suppliers[1]),

    "\nSupplies: {}".format(suppliers[2]),

    "\nExpected Delivery: {}".format(suppliers[3]),
    
    "\nActual Delivery: {}".format(suppliers[4])
    )
db.close()
