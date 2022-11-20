from flask import Flask, request
from connection_db import Connection
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

    Connection.request_functions(curs_functions)
    functions = curs_functions.fetchall()
    curs_functions.close()

    Connection.disconnect_db(conn)

    return f""" PELICULAS
                {movies} 
                FUNCIONES:
                {functions}"""
    
        
    
