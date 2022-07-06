'''Wendy Rodriguez
July 5, 2022
Module 9.3 Assignment'''

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

# Insert new record into Player table for Team Gandalf

cursor = db.cursor()
cursor.execute('INSERT INTO player (first_name, last_name, team_id) VALUES ("Smeagol", "Shire Folk", 1)')

# Create a SELECT query for Player records

cursor.execute('SELECT player_id, first_name, last_name, team_name FROM Player INNER JOIN Team ON Player.team_id = Team.team_id')
players = cursor.fetchall()

# Print output of a SELECT query after the INSERT INTO command

print("\n-- DISPLAYING PLAYERS AFTER INSERT --")
for player in players:
    print("Player ID: {}".format(player[0]), "\nFirst Name: {}".format(player[1]), "\nLast Name: {}".format(player[2]), 
    "\nTeam Name: {}\n".format(player[3]))

# Update inserted player to Team Sauron

cursor.execute('UPDATE player SET team_id = 2, first_name = "Gollum", last_name = "Ring Stealer" WHERE first_name = "Smeagol"')

# Create a SELECT query for Player records

cursor.execute('SELECT player_id, first_name, last_name, team_name FROM Player INNER JOIN Team ON Player.team_id = Team.team_id')
players = cursor.fetchall()

# Print output of a SELECT query after the UPDATE command

print("\n-- DISPLAYING PLAYERS AFTER UPDATE --")
for player in players:
    print("Player ID: {}".format(player[0]), "\nFirst Name: {}".format(player[1]), "\nLast Name: {}".format(player[2]), 
    "\nTeam Name: {}\n".format(player[3]))

# Delete inserted player

cursor.execute("DELETE from player WHERE first_name = 'Gollum'")

cursor.execute('SELECT player_id, first_name, last_name, team_name FROM Player INNER JOIN Team ON Player.team_id = Team.team_id')
players = cursor.fetchall()

# Print output of a SELECT query after the DELETE command

print("\n-- DISPLAYING PLAYERS AFTER DELETE --")
for player in players:
    print("Player ID: {}".format(player[0]), "\nFirst Name: {}".format(player[1]), "\nLast Name: {}".format(player[2]), 
    "\nTeam Name: {}\n".format(player[3]))
print("\n\n Press any key to continue...")