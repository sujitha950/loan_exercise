from ctypes.wintypes import CHAR, INT
import psycopg2

# con = psycopg2.connect(database="PostgresSQL", user="q2c_user", password="passw0rd", host="f5fc7f6b-efd4-4ee7-a84b-332e38adf2a5.c9v3nfod0e3fgcbd1oug.databases.appdomain.cloud", port="30835")
conn = psycopg2.connect(
      database="q2c", 
      user='q2c_user', 
      password='passw0rd', 
      host='f5fc7f6b-efd4-4ee7-a84b-332e38adf2a5.c9v3nfod0e3fgcbd1oug.databases.appdomain.cloud', 
      port= '30835'
      )
print("Database opened successfully")

cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS EMPLOYEE")
# sql =""" CREATE TABLE EMPLOYEE( CHAR(20) NOT NULL,LAST_NAME CHAR(20),AGE INT,SEX CHAR(1),INCOME FLOAT)"""
sql =""" CREATE TABLE EMPLOYEE(LOAN INT,TERM INT,LOAN_STATUS CHAR(20))"""
cur.execute(sql)
print("Table created successfully........")
conn.commit()
cur.execute('''INSERT INTO EMPLOYEE(LOAN,TERM,LOAN_STATUS) VALUES ( 20000,36,'notpaid')''')
cur.execute('''INSERT INTO EMPLOYEE(LOAN,TERM,LOAN_STATUS) VALUES ( 30000,24,'Fullypaid')''')
cur.execute('''INSERT INTO EMPLOYEE(LOAN,TERM,LOAN_STATUS) VALUES ( 40000,36,'notpaid')''')
cur.execute('''INSERT INTO EMPLOYEE(LOAN,TERM,LOAN_STATUS) VALUES ( 50000,36,'notpaid')''')
cur.execute('''INSERT INTO EMPLOYEE(LOAN,TERM,LOAN_STATUS) VALUES ( 60000,36,'notpaid')''')
cur.execute('''INSERT INTO EMPLOYEE(LOAN,TERM,LOAN_STATUS) VALUES ( 80000,12,'Fullypaid')''')
cur.execute('''INSERT INTO EMPLOYEE(LOAN,TERM,LOAN_STATUS) VALUES ( 90000,12,'Fullypaid')''')
cur.execute('''INSERT INTO EMPLOYEE(LOAN,TERM,LOAN_STATUS) VALUES ( 100000,36,'notpaid')''')
conn.commit()
print("Records inserted........")
cur.execute('''SELECT * from EMPLOYEE''')
result = cur.fetchall();
print(result)
cur.execute('''ALTER TABLE EMPLOYEE ADD COLUMN newterm INT ''')
conn.commit()
print("column added........")
for eachdetail in result:
    print(eachdetail)
    ternval=eachdetail[1]
    if ternval==36 and eachdetail[2]!="Fullypaid":
        print(eachdetail[1])
        loan=eachdetail[0]
        term=eachdetail[1]
        print(eachdetail[0])
        
        #Preparing the query to update the records
        sqlupdate = '''UPDATE EMPLOYEE SET newterm = term+12  WHERE LOAN = loan AND TERM = term AND LOAN_STATUS != 'Fullypaid' '''
        cur.execute(sqlupdate)

cur.execute('''SELECT * from EMPLOYEE''')
resultfinal = cur.fetchall();
print(resultfinal)
cur.execute('''ALTER TABLE EMPLOYEE ADD COLUMN int_rates_add_2pct FLOAT ''')
conn.commit()
print("column added........")
for eachdetailintrst in resultfinal:
    
    sqlupdate = '''UPDATE EMPLOYEE SET int_rates_add_2pct = loan*(1+0.02*term)  WHERE LOAN = loan AND TERM = term  '''
    cur.execute(sqlupdate)

cur.execute('''SELECT * from EMPLOYEE''')
results = cur.fetchall();
print(results)
# sql = "COPY (SELECT * FROM EMPLOYEE ) TO STDOUT WITH CSV DELIMITER ';'"
sql = "COPY (SELECT * FROM EMPLOYEE ) TO STDOUT WITH CSV HEADER"
with open(r"C:\\Users\\z0014225\\OneDrive - ZF Friedrichshafen AG\Desktop\\IBM\\sqltofile.csv", "w") as file:
    cur.copy_expert(sql, file)
print("Done")



