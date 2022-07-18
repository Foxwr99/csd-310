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
cursor.execute('SELECT name, wine FROM distributors')

# Create a report of distributors and which wine they sell

distributors = cursor.fetchall()
print("--- LIST OF DISTRIBUTORS AND THE WINE THEY CARRY ---")
for distributor in distributors:
    print("\nDistributor Name: {}".format(distributor[0]), "\nWine: {}".format(distributor[1]))
print()
print("Press any key to continue...")
print()
# Create a report showing how many distributors are selling each wine

print("--- LIST OF HOW MANY DISTRIBUTORS CARRY EACH WINE ---")
cursor.execute('SELECT wine, COUNT(wine) AS num FROM distributors GROUP BY wine HAVING COUNT(wine) > 0')
wines = cursor.fetchall()
for wine in wines:
    print("\nNumber of Distributors: {}".format(wine[1]), "\nWine: {}".format(wine[0]))
print()
print("Press any key to continue...")
    