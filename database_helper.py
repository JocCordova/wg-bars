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

	sql_create_items_table = """CREATE TABLE IF NOT EXISTS tasks (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    bought_by integer NOT NULL,
                                    date text NOT NULL,
                                    FOREIGN KEY (bought_by) REFERENCES Users (id)
                                );"""

    # create a database connection
	conn = create_connection(full_db_path)

    # create tables
	if conn is not None:
        # create projects table
		create_table(conn, sql_create_users_table)

        # create tasks table
		create_table(conn, sql_create_items_table)
	else:
		print("Error! cannot create the database connection.")


if __name__ == '__main__':
	main()
