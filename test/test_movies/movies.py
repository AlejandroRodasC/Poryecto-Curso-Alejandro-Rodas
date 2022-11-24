from connection_db import Connection

def requestMovies():

    if check_billboard():
        raise Exception('No movies available.')
        
    return 'Here are the available movies and their functions'


def check_billboard():
    conn = Connection.connect_db()
    curs_movies = conn.cursor(dictionary= True,buffered=True)
    Connection.request_movies(curs_movies)
    movies = curs_movies.fetchall()  
    if movies is None: #if billboard is empty
        return True
    else:
        return False