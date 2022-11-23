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

    def seat_verification(data):
        connec = conn.connect(host='localhost', user='root', passwd = 'alejandro', db='cine')
        request = 'SELECT * FROM Tickets where seat = %s and ID_FUNC = %s'
        cursor = connec.cursor()
        cursor.execute(request,data)
        if cursor.fetchone() is not None: #If the cursor is not empty 
            return True #return True to say that the seat is used
        else:
            return False
    
    def buy_the_ticket(data):
        connec = conn.connect(host='localhost', user='root', passwd = 'alejandro', db='cine')
        request = 'INSERT INTO Tickets (ID_USER , ID_MOV , ID_FUNC , seat , created_at) VALUES (%s,%s,%s,%s,%s)'
        cursor = connec.cursor()
        cursor.execute(request,data)
        connec.commit()
    
    def consult_tickets(cursor,data):
        request = (' SELECT Tickets.id_ticket , Tickets.seat , Functions.id_funct, Functions.date_funct,' 
                    'Movies.id_movie, Movies.title , Movies.poster , Movies.clasif from Tickets inner join Functions on Tickets.ID_FUNC = Functions.id_funct '
                    'inner join Movies where Tickets.ID_USER = %s and Functions.Id_movie = Movies.id_movie')
        cursor.execute(request,data)

    def check_ticket_date(data_ticket,date_now):
        connec = conn.connect(host='localhost', user='root', passwd = 'alejandro', db='cine')
        request = (' select Functions.date_funct from Functions inner join Tickets on Functions.id_funct = Tickets.ID_FUNC '
                    'where Tickets.id_ticket = %s')
        cursor = connec.cursor(dictionary=True)
        cursor.execute(request,data_ticket)
        ticket = cursor.fetchone()
        date_function_ticket = ticket['date_funct']
        if date_function_ticket < date_now: #If the ticket's date is less than today's date
            return True
        else:
            return False

    def verify_property_ticket(data):
        connec = conn.connect(host='localhost', user='root', passwd = 'alejandro', db='cine')
        request = ('Select * from Tickets where Tickets.ID_USER = %s and Tickets.id_ticket = %s')
        cursor = connec.cursor(dictionary=True)
        cursor.execute(request,data)
        ticket = cursor.fetchone()
        if ticket is None: #If there is a ticket with the user id and ticket id indicated 
            return True
        else:
            return False

    def delete_ticket(data):
        connec = conn.connect(host='localhost', user='root', passwd = 'alejandro', db='cine')
        request = ('DELETE FROM Tickets where Tickets.ID_USER = %s and Tickets.id_ticket = %s')
        cursor = connec.cursor()
        cursor.execute(request,data)
        connec.commit()