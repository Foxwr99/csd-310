'''Wendy Rodriguez
July 4, 2022
Module 9.2 Assignment'''


import mysql.connector

# Connect to pysports Database

config = {
    "user": "root",
    "password": "password123",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}


db = mysql.connector.connect(**config)
print("\n Database user {} connected to MySQL on host {} with database {}" .format(config["user"], config["host"], config["database"]))
print("\n\n Press any key to continue...")

# Create a cursor to INNER JOIN Player and Team tables by team_id

cursor = db.cursor()
cursor.execute('SELECT player_id, first_name, last_name, team_name FROM Player INNER JOIN Team ON Player.team_id = Team.team_id')

players = cursor.fetchall()

# Display results of INNER JOIN query

print("\n-- DISPLAYING PLAYER RECORDS --")
for player in players:
    print("Player ID: {}".format(player[0]), "\nFirst Name: {}".format(player[1]), "\nLast Name: {}".format(player[2]), 
    "\nTeam Name: {}\n".format(player[3]))

print('\nPress any key to continue...')

db.close()