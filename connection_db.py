import mysql.connector as conn
 
class Connection:
    def connect_db():
        connec = conn.connect(host='localhost', user='root', passwd = 'alejandro', db='cine')
        return connec
   
    def disconnect_db(connec):
        connec.close()
        return 'Se ha cerrado la base de datos'
    
    def request_movies(cursor):
        cursor.execute('Select * from Movies')
        return
    
    def request_functions(cursor):
        request = 'SELECT * FROM Functions '
        cursor.execute(request)

    def insert_users(connection,cursor,data):
        request = 'INSERT INTO Users (name_user, last_name , password_user, email, phone_number, created_at ) VALUES (%s,%s,%s,%s,%s,%s)' 
        cursor.execute(request,data)
        connection.commit()