from user import register_user
from user_factory import UserFactory
from connection_db import Connection
import pytest

class TestRegisterUser:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.user_data = UserFactory.create()
    
    #Happy Path 
    def test_user_is_registered(self):
        name_user = self.user_data['name_user']
        last_name =  self.user_data['last_name']
        password = self.user_data['password_user']
        email = self.user_data['email']
        phone_number = self.user_data['phone_number']
        created_at = self.user_data['created_at']
        data = (name_user,last_name,password,email,phone_number,created_at)

        message = register_user(**self.user_data)

        assert message == 'User succesfully registered'
        
        conn = Connection.connect_db()
        curs_users = conn.cursor()
        Connection.insert_users(conn,curs_users,data)
        Connection.disconnect_db(conn)

    #Edge Cases
    def test_the_name_length_is_more_than_40(self):
        with pytest.raises(Exception) as error:
            self.user_data['name_user'] = 'This is a name with more than 40 characters AAAAAAAAAAAAAAAAAAAAAAAAA'

            message = register_user(**self.user_data)
            assert str(error.value) == 'The username is longer than 40 characters.'
    
    def test_the_lastname_length_is_more_than_40(self):
        with pytest.raises(Exception) as error:
            self.user_data['last_name'] = 'This is a lastname with more than 40 characters AAAAAAAAAAAAAAAAAAAAAAAAA'

            message = register_user(**self.user_data)
            assert str(error.value) == 'The user\'s lastname is longer than 40 characters.'
    
    def test_the_password_length_is_more_than_30(self):
        with pytest.raises(Exception) as error:
            self.user_data['password_user'] = 'This is a password with more than 30 characters'

            message = register_user(**self.user_data)
            assert str(error.value) == 'The user\'s password is longer than 30 characters.'

    def test_invalid_format_email(self):
        with pytest.raises(Exception) as error:
            self.user_data['email'] = 'Invalid format email.'

            message = register_user(**self.user_data)
            assert str(error.value) == 'Incorrect email format.'

    def test_invalid_format_phone_number(self):
        with pytest.raises(Exception) as error:
            self.user_data['phone_number'] = 'Invalid format phone number.'

            message = register_user(**self.user_data)
            assert str(error.value) == 'The phone number has characters that are not digits or is longer than 15 digits.'