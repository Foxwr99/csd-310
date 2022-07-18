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
cursor=db.cursor()

db = mysql.connector.connect(**config)
print("--DISPLAYING EMPLOYEE TABLE--")
cursor = db.cursor()
cursor.execute("SELECT employee_id, name, department, quarterly_hours_q1, quarterly_hours_q2, quarterly_hours_q3, quarterly_hours_q4, total_hours FROM employees") 
employeelist = cursor.fetchall()
for employees in employeelist:
        print("\nEmployee ID: {}".format(employees[0]),

        "\nName: {}".format(employees[1]),

        "\nDepartment: {}".format(employees[2]),

        "\nQuarter 1 Hours: {}".format(employees[3]),

        "\nQuarter 2 Hours: {}".format(employees[4]),

        "\nQuarter 3 Hours: {}".format(employees[5]),

        "\nQuarter 4 Hours: {}".format(employees[6]),
        
        "\nTotal Hours: {}" .format(employees[7]))


