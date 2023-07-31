# Rick Jansen
# CYBR 410
# Module 9.3 Assignment: PySports: Update & Deletes
# July 30, 2023

# connectors
import mysql.connector
from mysql.connector import errorcode

# host configuration
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

# define variable show_players
def show_players(cursor, title):

    # inner join player table
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    # fetch cursor for players variable
    players = cursor.fetchall()

    print("\n  -- {} --".format(title))
    
    # iterate player results
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

# try/catch
try:

    db = mysql.connector.connect(**config)

    cursor = db.cursor()

    # add player to table
    add_player = ("INSERT INTO player(first_name, last_name, team_id)"
                 "VALUES(%s, %s, %s)")

    player_data = ("Smeagol", "Shire Folk", 1)

    cursor.execute(add_player, player_data)

    db.commit()

    # display updated player table
    show_players(cursor, "DISPLAYING PLAYERS AFTER INSERT")

    # update players
    update_player = ("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")

    cursor.execute(update_player)

    # display updated player table
    show_players(cursor, "DISPLAYING PLAYERS AFTER UPDATE")

    # delete player
    delete_player = ("DELETE FROM player WHERE first_name = 'Gollum'")

    cursor.execute(delete_player)

    # display updated player table
    show_players(cursor, "DISPLAYING PLAYERS AFTER DELETE")

    input("\n\n  Press any key to continue... ")

# error exception
except mysql.connector.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

# close
finally:

    db.close()
