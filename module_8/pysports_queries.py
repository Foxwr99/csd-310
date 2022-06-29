import mysql.connector
from mysql.connector import errorcode

# Set up configuration to connect to database pysports

config = {
    "user": "root",
    "password": "password123",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

db = mysql.connector.connect(**config)
print("\n Database user {} connected to MySQL on host {} with database {}" .format(config["user"], config["host"], config["database"]))
print()

print("-- DISPLAYING TEAM RECORDS --")

# Create cursor to fetch Team information from Team table in pysports database

cursor = db.cursor()
cursor.execute('SELECT team_id, team_name, mascot FROM team')

# Print results from SELECT statement

teams = cursor.fetchall()

for team in teams:
    print("Team ID: {}".format(team[0]), "\nTeam Name: {}".format(team[1]), "\nMascot: {}\n".format(team[2]))

print("\n-- DISPLAYING PLAYER RECORDS --")

# Create a cursor to fetch Player information from Player table in pysports database

cursor = db.cursor()
cursor.execute('SELECT player_id, first_name, last_name, team_id FROM player')

# Print results from SELECT statement

players = cursor.fetchall()

for player in players:
    print("Player ID: {}".format(player[0]), "\nFirst Name: {}".format(player[1]), 
    "\nLast Name: {}".format(player[2]), "\nTeam ID: {}\n".format(player[3]))

print()
print("Press any key to continue...")

db.close()