from connection_db import Connection
from datetime import datetime
ticket_data = None

def buy_ticket(
    id_ticket,
    ID_USER,
    ID_MOV,
    ID_FUNC,
    seat,
    created_at
):
    if check_id_user(ID_USER):
        raise Exception('The user does not exist.')
    if check_id_movie(ID_MOV):
        raise Exception('The movie does not exist.')
    if check_function(ID_MOV,ID_FUNC):
        raise Exception (f'The movie does not have a function with ID = {ID_FUNC}')
    if check_seat(ID_FUNC,seat):
        raise Exception (f'The seat {seat} for movie {ID_MOV} in the function {ID_FUNC} is used.')

    return 'The ticket was bought.'

def request_tickets(ID_USER):
    if check_user_tickets(ID_USER):
        raise Exception('The user has not tickets purchased.')

    return 'Here are your tickets'

def delete_tickets(ID_USER,id_ticket):
    if ticket_ownership(ID_USER,id_ticket):
        raise Exception(f'The ticket with id {id_ticket} does not belong to user with id {ID_USER}')

    if ticket_date(id_ticket):
        raise Exception(f'The ticket with the id {id_ticket} has already expired. You can not delete it.')

    return 'The tickets were eliminated'

def check_id_user(ID_USER):
    data =  (ID_USER,)
    request =  'Select * from Users where id_user = %s'
    conn = Connection.connect_db()
    cursor_us =  conn.cursor(dictionary=True)
    cursor_us.execute(request,data)
    cursor_us.fetchone()
    Connection.disconnect_db(conn)
    if cursor_us is not None:
        return False
    else: 
        return True

def check_id_movie(ID_MOV):
    data =  (ID_MOV,)
    request =  'Select * from Movies where id_movie = %s'
    conn = Connection.connect_db()
    cursor_mov =  conn.cursor(dictionary=True)
    cursor_mov.execute(request,data)
    cursor_mov.fetchone()
    Connection.disconnect_db(conn)
    if cursor_mov is not None:
        return False
    else: 
        return True

def check_function(ID_MOV, ID_FUNC):
    data =  (ID_MOV, ID_FUNC)
    request =  'Select * from Functions where ID_movie = %s and id_funct = %s'
    conn = Connection.connect_db()
    cursor_func =  conn.cursor(dictionary=True)
    cursor_func.execute(request,data)
    cursor_func.fetchone()
    Connection.disconnect_db(conn)
    if cursor_func is not None:
        return False
    else: 
        return True

def check_seat(ID_FUNC, seat):
    data = (seat, ID_FUNC)
    flag_seat_used = Connection.seat_verification(data)
    return flag_seat_used

def check_user_tickets(ID_USER):
    data = (ID_USER,)
    conn = Connection.connect_db()
    cursor_ticket = conn.cursor(dictionary=True)
    Connection.consult_tickets(cursor_ticket,data)
    cursor_ticket.fetchall()
    Connection.disconnect_db(conn)
    if cursor_ticket is None:
        return True
    else: 
        return False

def ticket_ownership(ID_USER, id_ticket):
    data = (ID_USER,id_ticket)
    flag = Connection.verify_ticket_ownership(data)
    return flag

def ticket_date(id_ticket):
    data = (id_ticket,)
    date = datetime.now()
    flag_date = Connection.check_ticket_date(data,date)
    return flag_date