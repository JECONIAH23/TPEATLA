class User:
    __username = ""
    __password = ""

    def login(self):
        print(f"{self.__username} logged in")
    def logout(self):
        Timestamp = ""
        print(f"USer {self.username} llogged out at {Timestamp}")

def add_user(data,tbl='users'):
    
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
                ff = "{}\tRecord inserted successfully into Laptop table".format(str(datetime.now()))
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
