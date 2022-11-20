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

