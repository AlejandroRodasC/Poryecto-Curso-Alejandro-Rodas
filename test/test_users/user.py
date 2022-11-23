from datetime import datetime
import random
import re
user_data = None

def register_user(
    id_user,
    name_user ,
    last_name ,
    password_user ,
    email ,
    phone_number,
    created_at       
):
    global user_data
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
    id_user= random.randint(0,999)
    created_at =  datetime.now()
    user_data = {
        'id_user' : id_user,
        'name_user' : name_user,
        'last_name' : last_name,
        'password_user' : password_user,
        'email' : email,
        'phone_number' : phone_number,
        'created_at' : created_at
    }

    return 'User succesfully registered'


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