import sqlite3
#connect to database
conn = sqlite3.connect("student.db")
#create cursor object to insert record

cursor = conn.cursor()

table ="""
Create table STUDENT(NAME, VARCHAR(25),CLASS VARCHAR(25), SECTION VARCHAR(25));
"""

cursor.execute(table)

##insert record

cursor.execute('''INSERT INTO STUDENT values ('krish','Data Science','A')''')
cursor.execute('''INSERT INTO STUDENT values ('Sudhanshu','Data Science','B')''')
cursor.execute('''INSERT INTO STUDENT values ('Darus','Data Science','A')''')
cursor.execute('''INSERT INTO STUDENT values ('Vikas','DEVOPS','A')''')
cursor.execute('''INSERT INTO STUDENT values ('Ram','DEVOPS','A')''')


print("the inserted records are")
data = cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)
conn.commit()
conn.close()