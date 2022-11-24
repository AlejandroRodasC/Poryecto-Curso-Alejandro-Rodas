from faker import Faker
from datetime import datetime
import random

fake = Faker()
id = random.randint(0,999)
created_at = datetime.now()

class TicketFactory:
    def create():
        ticket_data = {
        'id_ticket' : id,
        'ID_USER' : fake.random_int(100,999),
        'ID_MOV' :  fake.random_int(100,999),
        'ID_FUNC' :  fake.random_int(100,999),
        'seat' : 'C9',
        'created_at' : created_at
        }

        return ticket_data