import mysql.connector
from mysql.connector import Error
from os import system as sys

def login():
    # Login sql
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='TPEATLA',
                                            user='admin',
                                            password='')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        # if connection.is_connected():
            # cursor.close()
            # connection.close()
            print("MySQL connection is closed")


#QUERIES OF COUNT
def getincidents():
    return 76
def getculprits():
    return 87
#QUERIES OF RECORDS

################################
# add info queries
def db(query):
    try:
        # Database information
        connection = mysql.connector.connect(host='localhost',
                                            database='adb',
                                            user='root',
                                            password='')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            
            # Execute query
            if query:
                # print(query)
                # result = cursor.execute(mySql_Create_Table_Query)
                result = cursor.execute(query)
            
            print("You're connected to database: ", record)

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def addincident(data,tbl='tbl'):
    
    if not data and not tbl:
        return None
    else:
        dt = makevar(data)
        # formating table formats
        query = f"INSERT INTO {tbl} (`docID`, `doc`, `pic`, `number`) VALUES ('{dt}')"
        
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='adb',
                                            user='root',
                                            password='')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute(f"select database();")
            record = cursor.fetchone()
            print(record)
            # Execute query
            if query:
                print(query)
                print(type(query))
                cursor = connection.cursor()
                cursor.execute('query')
                connection.commit()
                print(cursor.rowcount, "Record inserted successfully into Laptop table")
                
                result = cursor.fetchone()
            print(record)

            
            print("You're connected to database: ", record)
        
    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))
        ff = "Failed to insert into MySQL table {}".format(error)
        cmd = f"echo {ff}>>db_logs.txt"
        sys(cmd)
    finally:   
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    # return sql

def makevar(a):
    b= ""
    c= len(a)
    if c == 0:
        # return None
        s=a
    elif c ==1:
        # return str(a[0])
        s=c
    else:
   
        p=0
        for i in a:
            
            if p <c-1:
                
                b += str(i) + "' ,'"
            else:
                b+=str(i)
            p+=1
        return b
  
addincident([9,'testing',89,45],'tbl')