import sqlite3
from sqlite3 import Error
import os


def create_connection(db_file):
    #create a database connection to a SQLite database
	conn = None
	
	try:
		conn = sqlite3.connect(db_file)
		return conn
	except Error as e:
		print(e)

	return conn

def create_table(conn, create_table_sql):
    # create a table from the create_table_sql statement
    # conn: Connection object
    # create_table_sql: a CREATE TABLE statement
    
	try:
		c = conn.cursor()
		c.execute(create_table_sql)
	except Error as e:
		print(e)

def main():
	database = r"\db\database.db"
	full_db_path = os.getcwd() + database

	sql_create_users_table = """ CREATE TABLE IF NOT EXISTS Users (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL
                                    ); """

	sql_create_items_table = """CREATE TABLE IF NOT EXISTS ITEMS (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL
                                );"""
                                
	sql_create_bought_by_table = """ CREATE TABLE IF NOT EXISTS BOUGHT_BY (
                                        id integer PRIMARY KEY,
                                        user_id integer NOT NULL
                                        item_id integer NOT NULL
                                        date text,
                                        FOREIGN KEY (user_id) REFERENCES Users (id)
                                        FOREIGN KEY (item_id) REFERENCES Items (id)
                                    ); """

    # create a database connection
	conn = create_connection(full_db_path)

    # create tables
	if conn is not None:
		
		create_table(conn, sql_create_users_table)
		create_table(conn, sql_create_items_table)
		create_table(conn, sql_create_bought_by_table)
		
	else:
		print("Error! cannot create the database connection.")


if __name__ == '__main__':
	main()
