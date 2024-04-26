#from pickle import NONE
from sqlite3 import *
from sqlite3 import Error
from os import * 


def create_connect(path:str):             #path->путь
    connection=None 
    try: 
        connection=connect(path)
        print("Ühendus on olemas! ")
    except Error as e:
        print(f"Tekkis viga : {e}")
    return connection


def execute_query(connection,query):
    try:
        cursor=connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Tabel on loodud või andned on sisestatud")
    except Error as e:
        print(f"Tekkis viga : {e}")


def execute_read_query(connection,query):
    cursor=connection.cursor()
    result=None
    try:
        cursor.execute(query)
        result=cursor.fetchall()
        return result
    except Error as e:
        print(f"Tekkis viga : {e}")


def execute_insert_query(connection,data):
    query="INSERT INTO users(Name,Lastname,Age,Birthday,Gender,Email) VALUES(?,?,?,?,?,?)"
    cursor=connection.cursor()
    cursor.execute(query)
    connection.commit()


def dropTable(connection,table):
    try: 
        cursor=connection.cursor()
        cursor.execute(f"Drop table if exests {table}")
        connection.commit()
        print(f"Table {table} oli kustutatud")
    except Error as e:
        print(f"Tekkis viga : {e}")

create_users_table="""
CREATE TABLE IF NOT EXISTS users(
Id INTEGER PRIMARY KEY AUTOINCREMENT,
Name TEXT NOT NULL,
Lastname TEXT NOT NULL,
Age INTEGER NOT NULL,
Birthday DATE TIME NOT NULL,
Gender TEXT NOT NULL,
Email TEXT NOT NULL
)
"""



insert_users="""
INSERT INTO 
users(Name,Lastname,Age,Birthday,Gender,Email)
VALUES
('Valeria','Allik',17,'25-04-2007','female','allikvaleria@gmail.com'),
('Daria','Halchenko',17,'06-10-2006','female','dariah@gmail.com'),
('Alexandra','Semjonova',16,'24-10-2007','female','sasha@gmail.com'),
("Maks", "Svirilin", 18, "10-03-2006", "mees", "maksimSvirilin@gmail.com"),
("Anton", "Ivanov", 20, "17-06-2002", "mees", "antonivanov@gmail.com")
"""

select_users="SELECT * from users"


create_users_AutoSalontable="""
CREATE TABLE IF NOT EXISTS auto(
Id INTEGER PRIMARY KEY AUTOINCREMENT,
AutoModel TEXT NOT NULL,
Varv TEXT NOT NULL,
AutoNumber INTEGER NOT NULL,
AutoKattesaamisePaev DATE TIME NOT NULL,
Joud INTEGER NOT NULL,
OstjaEmail TEXT NOT NULL,
NameId INTEGER,
FOREIGN KEY (NameId) REFERENCES name (Id)
)
"""



insert_AutoSalontable="""
INSERT INTO 
users(AutoModel,Varv,AutoNumber,AutoKattesaamisePaev,Joud,OstjaEmail,Name)
VALUES
('BMW','Punane',"ABC123",'25-04-2024',500,'allikvaleria1@gmail.com',1),
('HONDA','Roheline',"123ABC",'06-10-2024',300,'dariah1@gmail.com',2),
('TOYOTA','Must',"777AAA",'24-10-2024',450,'sasha1@gmail.com',3),
('TESLA', "Punane", "456TTT", "10-03-2024", 250, "maksimSvirilin1@gmail.com",4),
('MUSTANG', "Hall", "876HTK", "17-06-2024", 600, "antonivanov1@gmail.com",5)
"""


select_auto="SELECT * from auto"


filename=path.abspath(__file__)
dbdir=filename.rstrip('andmebaasid.py')
dbpath=path.join(dbdir,"data.db")
conn=create_connect(dbpath)
execute_query(conn,create_users_table)
execute_query(conn,insert_users)
users=execute_read_query(conn,select_users)
print("Kautajate tabel : ")
for user in users:
    print(user)


execute_query(conn,create_users_AutoSalontable)
execute_query(conn,insert_AutoSalontable)
auto=execute_read_query(conn,select_auto)
print("AutoSalon tabel : ")
for autod in auto:
    print(autod)