import mysql.connector
# Connect to the database
config = {
    "user" : "winery_user",
    "password": "birdbox2022!",
    "host": "127.0.0.1",
    "database": "winery",
    "raise_on_warnings": True
}
db = mysql.connector.connect(**config)
cursor = db.cursor()
cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
cursor.execute("INSERT INTO distributors (distributor_id, name, wine, tracking_id, employee_id) VALUES ('1001', 'Wino Forever', 'Chardonnay', '345', SELECT employee_id FROM employees WHERE employee_id = 14)")
cursor.execute("INSERT INTO distributors (distributor_id, name, wine, tracking_id, employee_id) VALUES ('1002', 'Cellar Door', 'Merlot', '350', SELECT employee_id FROM employees WHERE employee_id = 14)")
cursor.execute("INSERT INTO distributors (distributor_id, name, wine, tracking_id, employee_id) VALUES ('1002', 'Cellar Door', 'Merlot', '350', SELECT employee_id FROM employees WHERE employee_id = 14)")
cursor.execute("INSERT INTO distributors (distributor_id, name, wine, tracking_id, employee_id) VALUES ('1003', 'The Cellar', 'Chablis', '355', SELECT employee_id FROM employees WHERE employee_id = 14)")
cursor.execute("INSERT INTO distributors (distributor_id, name, wine, tracking_id, employee_id) VALUES ('1004', 'Off DeVine', 'Cabernet', '360', SELECT employee_id FROM employees WHERE employee_id = 14)")
cursor.execute("INSERT INTO distributors (distributor_id, name, wine, tracking_id, employee_id) VALUES ('1005', 'Cloud Wine', 'Chardonnay', '365', SELECT employee_id FROM employees WHERE employee_id = 14)")
cursor.execute("INSERT INTO distributors (distributor_id, name, wine, tracking_id, employee_id) VALUES ('1006', 'Wine in a Million', 'Chardonnay', '370', SELECT employee_id FROM employees WHERE employee_id = 14)")
db.commit()
cursor.execute("SELECT distributor_id, name, wine, tracking_id FROM distributors") 
distributorlist = cursor.fetchall()
for distributors in distributorlist:
    print("\nDistributor ID: {}".format(distributors[0]),

     "\nName: {}".format(distributors[1]),

    "\nWine: {}".format(distributors[2]),

    "\nTracking ID: {}".format(distributors[3]))
db.close()