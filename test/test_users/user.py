import re
from connection_db import Connection

def register_user(
    id_user,
    name_user ,
    last_name ,
    password_user ,
    email ,
    phone_number,
    created_at       
):
    if check_name_length(name_user):
        raise Exception('The username is longer than 40 characters.')
    if check_last_name_length(last_name):
        raise Exception('The user\'s lastname is longer than 40 characters.')
    if check_password_user(password_user):
        raise Exception('The user\'s password is longer than 30 characters.')
    if check_email_user(email):
        raise Exception('Incorrect email format.')
    if check_phone_number(phone_number):
        raise Exception('The phone number has characters that are not digits or is longer than 30 characters.')
    
    return 'User succesfully registered'

def login(
    id_user,
    name_user ,
    last_name ,
    password_user ,
    email ,
    phone_number,
    created_at 
):
    if check_email_in_database(email):
        raise Exception(f'Does not exist a user with the email {email}.')
    if check_password_for_email_in_database(email,password_user):
        raise Exception('Password is incorrect.')

    return f'Welcome {name_user}.'

def check_name_length(name_user):
    if len(name_user)>40:
        return True
    return False

def check_last_name_length(last_name):
    if len(last_name)>40:
        return True
    return False

def check_password_user(password):
    if len(password)>30:
        return True
    return False

def check_email_user(email):
    pat = r"^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    if not re.match(pat, email):
        return True
    if len(email)>50:
        return True
    return False

def check_phone_number(phone_number):
    pat = r"\+?[0-9-]+\s?[0-9]+$$"
    if not re.match(pat,phone_number):
        return True
    if len(phone_number) > 15:
        return True
    return False

def check_email_in_database(email):
    data = (email,)
    conn = Connection.connect_db()
    curs_user = conn.cursor(dictionary=True)
    Connection.user(curs_user,data)
    curs_user.fetchone()
    Connection.disconnect_db(conn)
    if curs_user is not None:
        return False
    else:
        return True

def check_password_for_email_in_database(email,password):
    data = (email,password)
    conn = Connection.connect_db()
    curs_user = conn.cursor(dictionary=True)
    Connection.login(curs_user,data)
    curs_user.fetchone()
    Connection.disconnect_db(conn)
    if curs_user is not None:
        return False
    else:
        return True