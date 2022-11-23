from user import register_user
from faker import Faker
from datetime import datetime
import random

fake = Faker()
id = random.randint(0,999)
created_at = datetime.now()
class UserFactory:
    def create():
        user_data = {
        'id_user' : id,
        'name_user' : fake.first_name(),
        'last_name' : fake.last_name(),
        'password_user' : fake.name(),
        'email' : fake.email(),
        'phone_number' : str(fake.random_int(10000000,99999999)),
        'created_at' : created_at
        }
        register_user(**user_data)

        return user_data