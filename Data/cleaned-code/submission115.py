import sqlite3

def create_connection(db_file):
                                                        
    conn = sqlite3.connect(db_file)
    return conn

def create_table(conn):
                                      
    sql_create_employees_table =\
\
\
\
                                         
    try:
        c = conn.cursor()
        c.execute(sql_create_employees_table)
    except sqlite3.Error as e:
        print(e)

def insert_employee(conn, employee):
                                                    
    sql =\
                             
    cur = conn.cursor()
    cur.execute(sql, employee)
    conn.commit()
    return cur.lastrowid

def select_all_employees(conn):
                                           
    cur = conn.cursor()
    cur.execute("SELECT * FROM employees")

    rows = cur.fetchall()
    for row in rows:
        print(row)

def main():
                                                  
    database = "company.db"

    conn = create_connection(database)
    with conn:
        create_table(conn)
        employee = ('Bob', 45)
        insert_employee(conn, employee)
        print("Employees in the database:")
        select_all_employees(conn)

if __name__ == '__main__':
    main()
