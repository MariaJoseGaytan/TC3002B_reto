import sqlite3

def create_connection(db_file):
                                                                              
    conn = sqlite3.connect(db_file)
    return conn

def create_table(conn):
                                  
    sql_create_users_table =\
\
\
\
                                     
    try:
        c = conn.cursor()
        c.execute(sql_create_users_table)
    except sqlite3.Error as e:
        print(e)

def insert_user(conn, user):
                                            
    sql =\
                             
    cur = conn.cursor()
    cur.execute(sql, user)
    conn.commit()
    return cur.lastrowid

def select_all_users(conn):
                                       
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")

    rows = cur.fetchall()
    for row in rows:
        print(row)

def main():
                                                  
    database = "test.db"

    conn = create_connection(database)
    with conn:
        create_table(conn)
        user = ('John', 28)
        insert_user(conn, user)
        print("Users in the database:")
        select_all_users(conn)

if __name__ == '__main__':
    main()
