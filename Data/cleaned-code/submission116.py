import sqlite3
from sqlite3 import Error

def create_connection(db_file):
\
\
       
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connection to {db_file} successful.")
    except Error as e:
        print(f"Error: {e}")
    return conn

def create_table(conn):
\
\
       
    sql_create_patients_table =\
\
\
\
                                        
    try:
        c = conn.cursor()
        c.execute(sql_create_patients_table)
        print("Table 'patients' created successfully.")
    except Error as e:
        print(f"Error: {e}")

def insert_patient(conn, patient):
\
\
       
    sql =\
                             
    cur = conn.cursor()
    cur.execute(sql, patient)
    conn.commit()
    return cur.lastrowid

def select_all_patients(conn):
\
\
       
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM patients")
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print(f"Error: {e}")

def main():
\
\
       
    database = "hospital.db"                        

    conn = create_connection(database)
    if conn is not None:
        create_table(conn)
        patient = ('Alice', 30)
        insert_patient(conn, patient)
        print("Patients in the database:")
        select_all_patients(conn)
    else:
        print("Error! Cannot create the database connection.")

if __name__ == '__main__':
    main()
