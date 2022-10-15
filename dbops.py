import sqlite3

dbh=sqlite3.connect("jumio.db")
cursorObject=dbh.cursor()

def create_table():
    cursorObject.execute("CREATE TABLE employee(empname TEXT,exp REAL,tech TEXT)")

def load_data():
    #cursorObject.execute("INSERT INTO employee VALUES('Raghul Ramesh',16,'Python')")
    #cursorObject.execute("INSERT INTO employee VALUES('Balamurugan',21,'Bigdata')")
    e_name=input("Enter your name:")
    e_exp=int(input("Enter your experience:"))
    e_tech=input("Enter your technology:")
    #cursorObject.execute("SET AUTOCOMMIT ON ")
    cursorObject.execute("INSERT INTO employee VALUES(?,?,?)",(e_name,e_exp,e_tech))

def update_data():
    cursorObject.execute("UPDATE employee set tech='Python' WHERE empname='Malini'")

def delete_data():
    cursorObject.execute("DELETE FROM employee WHERE empname='Khushal' ")
#create_table()
# for x in range(5):
#     load_data()

def fetch_data():
    cursorObject.execute("SELECT * FROM employee")
    # fetchonprint(cursorObject.fetchone())e, fetchmany, fetchall
    #print(cursorObject.fetchone())
    #print(cursorObject.fetchmany(2))
    #print(cursorObject.fetchall())
    for rows in cursorObject.fetchall():
        print(rows[0] + " ===> "+ rows[2] + " ===> " + str(rows[1]))
#update_data()
#delete_data()
#fetch_data()
dbh.commit()
cursorObject.close()
dbh.close()