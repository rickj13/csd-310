# Rick Jansen
# CYBR 410
# Module 8.3 Assignment: PySports: Table Queries
# July 23, 2023


# connectors
import mysql.connector
from mysql.connector import errorcode

#host configuration
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

#try/catch
try:
  
    db = mysql.connector.connect(**config)

    cursor = db.cursor()

    #query team table 
    cursor.execute("SELECT team_id, team_name, mascot FROM team")

    #fetch cursor for teams variable 
    teams = cursor.fetchall()

    print("\n  -- DISPLAYING TEAM RECORDS --")
    
    #iterate team, results 
    for team in teams: 
        print("  Team ID: {}\n  Team Name: {}\n  Mascot: {}\n".format(team[0], team[1], team[2]))

    #query player table 
    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")

    #fetch cursor for players variable 
    players = cursor.fetchall()

    print ("\n  -- DISPLAYING PLAYER RECORDS --")

    #iterate player, results
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team ID: {}\n".format(player[0], player[1], player[2], player[3]))

    input("\n\n  Press any key to continue... ")

#error exception
except mysql.connector.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

#close
finally:
    
    db.close()
  
