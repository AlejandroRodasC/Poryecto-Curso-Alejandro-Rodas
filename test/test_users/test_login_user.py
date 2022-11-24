from user import login
from user_factory import UserFactory
import pytest

class TestLoginUser:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.user_data = UserFactory.create()
    
    #Happy Path
    def test_user_login(self):
        self.user_data['email'] = 'ejemplo1@gmail.com' #This email exists in the database.
        self.user_data['password_user'] = '2222' #And this is the password for that email.
        name = self.user_data['name_user']

        message = login(**self.user_data)

        assert message == f'Welcome {name}.'
    
    #Edge Cases
    def test_email_does_not_exit(self):
        with pytest.raises(Exception) as error:
            email =  self.user_data['email']
            message = login(**self.user_data)

            assert str(error.value)== f'Does not exist a user with the email {email}.'
    
    def test_password_is_incorrect(self):
        with pytest.raises(Exception) as error:
            message = login(**self.user_data)

            assert str(error.value) == 'Password is incorrect.'


