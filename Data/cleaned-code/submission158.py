import sqlite3

def connect_database(db_name):
                                                           
    connection = sqlite3.connect(db_name)
    return connection

def initialize_table(connection):
                                   
    create_table_query =\
\
\
\
                                 
    try:
        cursor = connection.cursor()
        cursor.execute(create_table_query)
    except sqlite3.Error as error:
        print(error)

def add_employee(connection, staff):
                                          
    insert_query =\
                                      
    cur = connection.cursor()
    cur.execute(insert_query, staff)
    connection.commit()
    return cur.lastrowid

def fetch_all_employees(connection):
                                               
    cur = connection.cursor()
    cur.execute("SELECT * FROM staff")

    records = cur.fetchall()
    for record in records:
        print(record)

def run_operations():
                                                 
    db_name = "organization.db"

    connection = connect_database(db_name)
    with connection:
        initialize_table(connection)
        staff = ('Alice', 38)
        add_employee(connection, staff)
        print("Current staff in the database:")
        fetch_all_employees(connection)

if __name__ == '__main__':
    run_operations()
