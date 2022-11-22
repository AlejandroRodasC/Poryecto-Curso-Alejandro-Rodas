from flask import Flask, request, jsonify
import jwt
from datetime import datetime
from connection_db import Connection
from methods import Methods
from functools import wraps
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
conn = Connection.connect_db()

def token_is_requiered(tok):
    @wraps(tok)
    def decorated(*args, **Kwargs):
        token  = request.args.get('Token')

        if not token:
           return jsonify({'message' : 'Token is missing'}) 

        try:
            data =  jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        except:
            return jsonify({'message' : 'Token is invalid'})

        return tok(*args, **Kwargs)
    return decorated

@app.route("/")
def index():
    return 'This is the start of the APP.'

@app.route('/exit')
def exit():
    Connection.disconnect_db(conn)
    return 'Come back soon :D'

@app.route('/movies_available')
def list_movies():   
    curs_movies = conn.cursor(dictionary= True,buffered=True)

    Connection.request_movies(curs_movies)
    movies = curs_movies.fetchall()
    curs_movies.close()

    return movies

@app.post('/register_user')    
def register_user():
    name = request.form['name_user']
    ls_name = request.form['last_name']
    passwd = request.form['password']
    email = request.form['email']
    pnum= request.form['phone_number']
    created_at = datetime.now()

    data = (name, ls_name,passwd,email,pnum,created_at)
    curs_users = conn.cursor()
    Connection.insert_users(conn,curs_users,data)

    curs_users.close()
    return 'The user is registered'

@app.post('/login')
def login():
    passwd = request.form['password']
    email = request.form['email']
    data = (email, passwd)
    curs_login = conn.cursor(dictionary=True)
    Connection.login(curs_login,data)
    user = curs_login.fetchone()
    id_user = user['id_user']
    if user is not None:
        token =  jwt.encode({'user_email': email , 'id_user' : id_user}, app.config['SECRET_KEY'], algorithm='HS256')
        return jsonify({'token': token})
    else:
        return 'The user does not exist.'

@app.post('/buy_tickets')
@token_is_requiered
def buy_tickets():
    token = request.args.get('Token')
    dict_user =  jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
    email_user = str(dict_user['user_email'])
    data_user = (email_user,)
    curs_user = conn.cursor(dictionary=True)
    Connection.user(curs_user,data_user)

    user = curs_user.fetchone()
    id_user = int(user['id_user'])
    id_movie =  int(request.form['id_movie'])
    id_function = int(request.form['id_function'])
    created_at = datetime.now()
    seating_string = request.form['seating']
    seating_array = seating_string.split(',')

    for seat in seating_array:
        flag = Methods.Review_seating(seat)
        if flag:
            return f'The seat {seat} does not exist'
        else:
            data_seat = (seat, id_function)
            flag_seat_used = Connection.seat_verification(data_seat)
        
        if flag_seat_used:
            return f'The seat {seat} is used.'
    
    for seat in seating_array:
        data_ticket = (id_user,id_movie,id_function,seat,created_at)
        Connection.buy_the_ticket(data_ticket)
    
    return f'The tickets were bought'

@app.get('/consult_tickets')
@token_is_requiered
def consult_tickets():
    token = request.args.get('Token')
    dict_user =  jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
    id_user = int(dict_user['id_user'])
    data = (id_user,)
    curs_tickets = conn.cursor(dictionary= True,buffered=True)

    Connection.consult_tickets(curs_tickets,data)
    tickets = curs_tickets.fetchall()
    curs_tickets.close()

    return tickets