from asyncio.windows_events import NULL
from distutils.log import info
import mysql.connector
from mysql.connector import Error
from os import system as sys
from datetime import datetime


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
                                    ################################
                                    #######                  #######
                                    #######  INSERT QUERIES  #######
                                    #######                  #######
                                    ################################
                                    ################################
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
                cursor.execute(query)
                connection.commit()
                print(cursor.rowcount, "Record inserted successfully into {}")
                ff = "{}\tRecord inserted successfully into {}".format(str(datetime.now()))
                cmd = f"echo {ff}>>db_logs.txt"
                sys(cmd)
                result = cursor.fetchone()
            print(record)

            
            print("You're connected to database: ", record)
        
    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))
        ff = "{}\tFailed to insert into MySQL table {}".format(str(datetime.now()),error)
        cmd = f"echo {ff}>>db_logs.txt"
        sys(cmd)
    finally:   
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    # return sql

def add_user(data=[NULL,'username','email', 'password', 'contact'],tbl='users'):
    
    if not data and not tbl:
        return None
    else:
        dt = makevar(data)
        # formating table formats
        query = f"INSERT INTO {tbl} (`userID`, `username`, `email`, `password`,`contact`) VALUES (NULL, '{dt}')"
        # sql = "INSERT INTO `users` (`userID`, `username`, `email`, `password`, `contact`) VALUES (NULL, 'admin', 'admin@system.sy', 'admin', '');"
        
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
                cursor.execute(query)
                connection.commit()
                print(cursor.rowcount, "Record inserted successfully into {}".format(tbl))
                ff = "{}\tRecord inserted successfully into {}".format(str(datetime.now()),tbl)
                cmd = f"echo {ff}>>db_logs.txt"
                sys(cmd)
                result = cursor.fetchone()
            print(record)

            
            print("You're connected to database: ", record)
        
    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))
        ff = "{}\tFailed to insert into MySQL table {}".format(str(datetime.now()),error)
        cmd = f"echo {ff}>>db_logs.txt"
        sys(cmd)
    finally:   
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    # return sql



def makevar(a):#Converts python list into comma separated string.
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


################ 
### incidents ##
################

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData


def insertBLOB(emp_id, name, photo, biodataFile):
    print("Inserting BLOB into python_employee table")
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='python_db',
                                             user='pynative',
                                             password='pynative@#29')

        cursor = connection.cursor()
        sql_insert_blob_query = """ INSERT INTO python_employee
                          (id, name, photo, biodata) VALUES (%s,%s,%s,%s)"""

        empPicture = convertToBinaryData(photo)
        file = convertToBinaryData(biodataFile)

        # Convert data into tuple format
        insert_blob_tuple = (emp_id, name, empPicture, file)
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        connection.commit()
        print("Image and file inserted successfully as a BLOB into python_employee table", result)

    except mysql.connector.Error as error:
        print("Failed inserting BLOB data into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

insertBLOB(1, "Eric", "D:\Python\Articles\my_SQL\images\eric_photo.png",
           "D:\Python\Articles\my_SQL\images\eric_bioData.txt")
insertBLOB(2, "Scott", "D:\Python\Articles\my_SQL\images\scott_photo.png",
           "D:\Python\Articles\my_SQL\images\scott_bioData.txt")
  

                                        ########################
                                        ### End Of Incidents ###
                                        ########################

################################
################################
#######                  #######
#######  SELECT QUERIES  #######
#######                  #######
################################
################################


def get_users(tbl='users'):
     
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
            query = 'select * FROM {};'.format(tbl)
            # Execute query
            if query:
                print(query)
                print(type(query))
                cursor = connection.cursor()
                cursor.execute(query)
                # connection.commit()
                info = cursor.fetchall()
                print(cursor.rowcount, "Record fetsched successfully from {} table".format(tbl))
                ff = "{}\tRecords inserted successfully from {}".format(str(datetime.now()),tbl)
                cmd = f"echo {ff}>>db_logs.txt"
                sys(cmd)
                record = cursor.fetchone()
            print(info)

            
            print("You're connected to database: ", record)
        
    except mysql.connector.Error as error:
        print("Failed to execute query on table{}".format(error))
        ff = "{}\tFailed to execute query on  MySQL table {}".format(str(datetime.now()),error)
        cmd = f"echo {ff}>>db_logs.txt"
        sys(cmd)
    finally:   
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    # return info


def get_incidents(tbl='incidents'):
     
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
            query = "select * FROM {};".format(tbl)

            # Execute query
            if query:
                print(query)
                print(type(query))
                cursor = connection.cursor()
                cursor.execute(query)
                # connection.commit()
                info = cursor.fetchall()
                print(cursor.rowcount, "Record fetsched successfully from {} table".format(tbl))
                ff = "{}\tRecords inserted successfully from {}".format(str(datetime.now()),tbl)
                cmd = f"echo {ff}>>db_logs.txt"
                sys(cmd)
                record = cursor.fetchone()
            print(info)
            return info
            
            print("You're connected to database: ", record)
        
    except mysql.connector.Error as error:
        print("Failed to execute query on table{}".format(error))
        ff = "{}\tFailed to execute query on  MySQL table {}".format(str(datetime.now()),error)
        cmd = f"echo {ff}>>db_logs.txt"
        sys(cmd)
    finally:   
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")



################################
################################
#######                  #######
#######  COUNT  QUERIES  #######
#######                  #######
################################
################################


################################
################################
#######                  #######
#######  TEST - QUERIES  #######
#######                  #######
################################
################################


# addincident([9,'testing',89,45],'tbl')
add_user(['samuel','samuel@ject.com','samuel1234','0774057306'],)
get_users()