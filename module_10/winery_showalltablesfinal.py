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
print("--DISPLAYING EMPLOYEE TABLE--")
cursor = db.cursor()
cursor.execute("SELECT employee_id, name, department, quarterly_hours FROM employees") 
employeelist = cursor.fetchall()
for employees in employeelist:
        print("\nEmployee ID: {}".format(employees[0]),

        "\nName: {}".format(employees[1]),

        "\nDepartment: {}".format(employees[2]),

        "\nQuarterly Hours: {}".format(employees[3]))

print()
print("--DISPLAYING DISTRIBUTOR TABLE--")
cursor.execute("SELECT distributor_id, name, wine, tracking_id FROM distributors") 
distributorlist = cursor.fetchall()
for distributors in distributorlist:
        print("\nDistributor ID: {}".format(distributors[0]),

        "\nName: {}".format(distributors[1]),

        "\nWine: {}".format(distributors[2]),

        "\nTracking ID: {}".format(distributors[3]))

print()
print("--DISPLAYING SUPPLIER TABLE--")
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
