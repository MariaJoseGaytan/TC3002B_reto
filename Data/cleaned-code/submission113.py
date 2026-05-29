import sqlite3

def create_connection(db_file):
                                                 
    conn = sqlite3.connect(db_file)
    return conn

def create_table(conn):
                                      
    sql_create_customers_table =\
\
\
\
                                         
    try:
        c = conn.cursor()
        c.execute(sql_create_customers_table)
    except sqlite3.Error as e:
        print(e)

def insert_customer(conn, customer):
                                                    
    sql =\
                             
    cur = conn.cursor()
    cur.execute(sql, customer)
    conn.commit()
    return cur.lastrowid

def select_all_customers(conn):
                                           
    cur = conn.cursor()
    cur.execute("SELECT * FROM customers")

    rows = cur.fetchall()
    for row in rows:
        print(row)

def main():
                                                  
    database = "customers.db"

    conn = create_connection(database)
    with conn:
        create_table(conn)
        customer = ('Alice', 32)
        insert_customer(conn, customer)
        print("Customers in the database:")
        select_all_customers(conn)

if __name__ == '__main__':
    main()
