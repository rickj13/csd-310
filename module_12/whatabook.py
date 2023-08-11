# Rick Jansen
# CYBR 410
# Module 12.3 Assignment: WhatABook
# August 12, 2023


# connectors
import sys
import mysql.connector
from mysql.connector import errorcode

# host configuration
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

# define variable show_menu
def show_menu():
    print("\n  -- Main Menu --")

    print("    1. View Books\n    2. View Store Locations\n    3. My Account\n    4. Exit Program")

    try:
        choice = int(input('      <Example: enter 1 for book listing>: '))

        return choice
    except ValueError:
        print("\n  Invalid number, program terminated...\n")

        sys.exit(0)

# define variable show_books
def show_books(_cursor):

    # inner join 
    _cursor.execute("SELECT book_id, book_name, author, details from book")

    # get results for cursor object 
    books = _cursor.fetchall()

    print("\n  -- DISPLAYING BOOK LISTING --")
    
    # display results 
    for book in books:
        print("  Book Name: {}\n  Author: {}\n  Details: {}\n".format(book[0], book[1], book[2]))

# define variable show_locations
def show_locations(_cursor):

    # inner join
    _cursor.execute("SELECT store_id, locale from store")

    # get results for cursor object
    locations = _cursor.fetchall()

    print("\n  -- DISPLAYING STORE LOCATIONS --")

    # display results
    for location in locations:
        print("  Locale: {}\n".format(location[1]))

# define variable validate_user
def validate_user():

    try:
        user_id = int(input('\n      Enter a customer ID <Example: enter 1 for user_id 1>: '))

        if user_id < 0 or user_id > 3:
            print("\n  Invalid customer number, program terminated...\n")
            sys.exit(0)

        return user_id
    except ValueError:
        print("\n  Invalid number, program terminated...\n")

        sys.exit(0)

# show account menu
def show_account_menu():

    try:
        print("\n      -- Customer Menu --")
        print("        1. Wishlist\n        2. Add Book\n        3. Main Menu")
        account_option = int(input('        <Example: enter 1 for wishlist>: '))

        return account_option
    except ValueError:
        print("\n  Invalid number, program terminated...\n")

        sys.exit(0)

# query books in wishlist
def show_wishlist(_cursor, _user_id):

    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(_user_id))
    
    wishlist = _cursor.fetchall()

    print("\n        -- DISPLAYING WISHLIST ITEMS --")

    for book in wishlist:
        print("        Book Name: {}\n        Author: {}\n".format(book[4], book[5]))

# query books not in wishlist
def show_books_to_add(_cursor, _user_id):

    query = ("SELECT book_id, book_name, author, details "
            "FROM book "
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))

    print(query)

    _cursor.execute(query)

    books_to_add = _cursor.fetchall()

    print("\n        -- DISPLAYING AVAILABLE BOOKS --")

    for book in books_to_add:
        print("        Book Id: {}\n        Book Name: {}\n".format(book[0], book[1]))

# add books to wishlist
def add_book_to_wishlist(_cursor, _user_id, _book_id):
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))

# try/catch block
try:

    # connect to the whatabook database
    db = mysql.connector.connect(**config)

    # for SQL queries
    cursor = db.cursor()

    print("\n  Welcome to the WhatABook Application! ")

    # show main menu
    user_selection = show_menu()

    # while loop selection not 4
    while user_selection != 4:

        # user selection 1 show books
        if user_selection == 1:
            show_books(cursor)

        # user selection 2 show locations
        if user_selection == 2:
            show_locations(cursor)

        # user selection 3 validate user
        if user_selection == 3:
            my_user_id = validate_user()
            account_option = show_account_menu()

            # while loop selection not 3
            while account_option != 3:

                # user selection 1 for books in wishlist 
                if account_option == 1:
                    show_wishlist(cursor, my_user_id)

                # user selection 2 for books not in wishlist
                if account_option == 2:

                    # show books not currently in wishlist
                    show_books_to_add(cursor, my_user_id)

                    # get book_id 
                    book_id = int(input("\n        Enter the ID of the book you want to add: "))
                    
                    # add book to wishlist
                    add_book_to_wishlist(cursor, my_user_id, book_id)

                    # commit changes
                    db.commit()

                    print("\n        Book id: {} was added to your wishlist!".format(book_id))

                # error for input outside 0-3 
                if account_option < 0 or account_option > 3:
                    print("\n      Invalid option, please retry...")

                # show account menu 
                account_option = show_account_menu()
        
        # error for input outside 0-4
        if user_selection < 0 or user_selection > 4:
            print("\n      Invalid option, please retry...")
            
        # show main menu
        user_selection = show_menu()

    print("\n\n  Program terminated...")

# error exception handling
except mysql.connector.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password is invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

# close
finally:

    db.close()
