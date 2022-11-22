import mysql.connector as conn
 
class Connection:
    
    def connect_db():
        connec = conn.connect(host='localhost', user='root', passwd = 'alejandro', db='cine')
        return  connec
   
    def disconnect_db(connec):
        connec.close()
        return 'Se ha cerrado la base de datos'
    
    def request_movies(cursor):
        request = ( 'select Movies.id_movie , Movies.title , Movies.poster , Movies.clasif , Functions.id_funct , Functions.date_funct from Movies ' 
        'INNER JOIN Functions on Movies.id_movie = Functions.ID_movie')
        cursor.execute(request)
        return
    
    def request_functions(cursor):
        request = 'SELECT * FROM Functions '
        cursor.execute(request)

    def insert_users(connection,cursor,data):
        request = 'INSERT INTO Users (name_user, last_name , password_user, email, phone_number, created_at ) VALUES (%s,%s,%s,%s,%s,%s)' 
        cursor.execute(request,data)
        connection.commit()
    
    def login(cursor,data):
        request = 'SELECT * FROM Users WHERE email = %s AND password_user = %s'
        cursor.execute(request,data)
    
    def user(cursor,data):
        request = 'SELECT * FROM Users WHERE email = %s'
        cursor.execute(request,data)

    def seat_verification(seat):
        connec = conn.connect(host='localhost', user='root', passwd = 'alejandro', db='cine')
        request = 'SELECT * FROM Tickets where seat = %s'
        cursor = connec.cursor()
        cursor.execute(request,seat)
        if cursor.fetchone() is not None:
            return True
        else:
            return False