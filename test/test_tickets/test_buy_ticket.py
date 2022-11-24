from tickets import buy_ticket
import pytest
from ticket_factory import TicketFactory
from connection_db import Connection
from datetime import datetime
class TestBuyTicket:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.ticket_data = TicketFactory.create()
    
    #Happy Path
    def test_buy_tickets(self):
        self.ticket_data['ID_USER'] = 1 #The user exist in database
        self.ticket_data['ID_MOV'] = 11 #The movie existe in database
        self.ticket_data['ID_FUNC'] = 555 #The function existe for that movie
        id_user =  1
        id_mov = 11
        id_func = 555
        seat  = self.ticket_data['seat']
        created_at = datetime.now()
        data=(id_user,id_mov,id_func,seat,created_at)

        message = buy_ticket(**self.ticket_data)

        assert message ==  'The ticket was bought.'

        conn = Connection.connect_db()
        Connection.buy_the_ticket(data)
        Connection.disconnect_db(conn)
    
    def test_user_id_does_not_exist(self):
        with pytest.raises(Exception) as error:
            message = buy_ticket(**self.ticket_data)

            assert str(error.value) == 'The user does not exist.'
    
    def test_movie_id_does_not_exist(self):
        self.ticket_data['ID_USER'] = 1
        with pytest.raises(Exception) as error:
            message = buy_ticket(**self.ticket_data)

            assert str(error.value) == 'The movie does not exist.'
    
    def test_function_id_does_not_exist(self):
        self.ticket_data['ID_USER'] = 1
        self.ticket_data['ID_MOV'] = 11
        ID_FUNC = self.ticket_data['ID_FUNC']
        with pytest.raises(Exception) as error:
            message = buy_ticket(**self.ticket_data)

            assert str(error.value) == f'The movie does not have a function with ID = {ID_FUNC}'
    
    def test_seat_is_used(self):
        self.ticket_data['ID_USER'] = 1 
        self.ticket_data['ID_MOV'] = 11 
        self.ticket_data['ID_FUNC'] = 555
        ID_FUNC = self.ticket_data['ID_FUNC']
        ID_MOV = self.ticket_data['ID_MOV']
        seat = self.ticket_data['seat']
        with pytest.raises(Exception) as error:
            message = buy_ticket(**self.ticket_data)

            assert str(error.value) == f'The seat {seat} for movie {ID_MOV} in the function {ID_FUNC} is used.'

