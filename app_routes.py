from flask import Flask, request
from connection_db import Connection
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def index():
    return 'This is the start of the program'

@app.route('/movies_available')
def list_movies():
    conn = Connection.connect_db()
    curs_movies = conn.cursor(dictionary= True,buffered=True)
    curs_functions = conn.cursor(dictionary = True, buffered=True)

    Connection.request_movies(curs_movies)
    movies = curs_movies.fetchall()
    curs_movies.close()

    Connection.disconnect_db(conn)
    return movies

@app.route('/register_user', methods = ['POST'])    
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
    
    
