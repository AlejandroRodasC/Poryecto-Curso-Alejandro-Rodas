from tickets import request_tickets
import pytest
from ticket_factory import TicketFactory


class TestRequestTickets:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.ticket_data = TicketFactory.create()

    #Happy Path
    def test_request_user_tickets(self):
        self.ticket_data['ID_USER'] = 1 #This user has tickets
        ID_USER = self.ticket_data['ID_USER']

        message = request_tickets(ID_USER)

        assert message ==  'Here are your tickets'
    
    #Edge case
    def test_the_user_does_not_have_tickets(self):
        ID_USER = 999
        with pytest.raises(Exception) as error:
            message = request_tickets(ID_USER)

            assert str(error.value) == 'The user has not tickets purchased.'