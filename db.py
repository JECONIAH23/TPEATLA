import mysql.connector
from mysql.connector import Error

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
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


#QUERIES OF COUNT
def getincidents():
    return 76
def getculprits():
    return 87
#QUERIES OF RECORDS
