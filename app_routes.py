from flask import Flask, request, jsonify
import jwt
import re
from datetime import datetime, timedelta
from connection_db import Connection
from functools import wraps
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'

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

@app.route('/movies_available')
def list_movies():
    conn = Connection.connect_db()
    curs_movies = conn.cursor(dictionary= True,buffered=True)

    Connection.request_movies(curs_movies)
    movies = curs_movies.fetchall()
    curs_movies.close()

    Connection.disconnect_db(conn)
    return movies

@app.post('/register_user')    
def register_user():
    name = request.form['name_user']
    ls_name = request.form['last_name']
    passwd = request.form['password']
    email = request.form['email']
    pnum= int(request.form['phone_number'])
    created_at = datetime.now()

    data = (name, ls_name,passwd,email,pnum,created_at)
    conn = Connection.connect_db()
    curs_users = conn.cursor()
    Connection.insert_users(conn,curs_users,data)

    curs_users.close()
    Connection.disconnect_db(conn)
    return 'The user is registered'

@app.post('/login')
def login():
    passwd = request.form['password']
    email = request.form['email']
    data = (email, passwd)
    conn = Connection.connect_db()
    curs_login = conn.cursor()
    Connection.login(curs_login,data)
    user = curs_login.fetchone()
    
    if user is not None:
        token =  jwt.encode({'user_email': email }, app.config['SECRET_KEY'], algorithm='HS256')
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
    conn = Connection.connect_db()
    curs_user = conn.cursor(dictionary=True)
    Connection.user(curs_user,data_user)

    user = curs_user.fetchone()
    id = user['id_user']
    id_movie =  int(request.form['id_movie'])
    id_function = int(request.form['id_function'])
    seating_string = request.form['seating']
    seating_array = seating_string.split(',')

    for seat in seating_array:
        pat = r"[A-E][0-9]$"
        
        if re.match(pat,seat):
            pass
        else:
            if '10' in seat :
                pass
            else:
                return f'The seat {seat} does not exist.'

    return jsonify({'message' : 'You can buy tickets'})

