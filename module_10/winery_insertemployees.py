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

cursor.execute("INSERT INTO employees (employee_id, name, department, quarterly_hours) VALUES ('10', 'Janet Collins', 'Finance', '500')")
cursor.execute("INSERT INTO employees (employee_id, name, department, quarterly_hours) VALUES ('11', 'Roz Murphy', 'Marketing', '550')")
cursor.execute("INSERT INTO employees (employee_id, name, department, quarterly_hours) VALUES ('12', 'Bob Ulrich', 'Marketing', '475')")
cursor.execute("INSERT INTO employees (employee_id, name, department, quarterly_hours) VALUES ('13', 'Henry Doyle', 'Production', '500')")
cursor.execute("INSERT INTO employees (employee_id, name, department, quarterly_hours) VALUES ('14', 'Maria Costanza', 'Distribution', '530')")
cursor.execute("INSERT INTO employees (employee_id, name, department, quarterly_hours) VALUES ('15', 'Stan Bucchus', 'Management', '600')")
db.commit()
cursor.execute("SELECT employee_id, name, department, quarterly_hours FROM employees") 
employeelist = cursor.fetchall()
for employees in employeelist:
    print("\nEmployee ID: {}".format(employees[0]),

     "\nName: {}".format(employees[1]),

     "\nDepartment: {}".format(employees[2]),

     "\nQuarterly Hours: {}".format(employees[3]))
db.close()
