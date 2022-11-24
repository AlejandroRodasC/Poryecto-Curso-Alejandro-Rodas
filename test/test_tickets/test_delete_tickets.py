from tickets import delete_tickets
import pytest
from ticket_factory import TicketFactory
from connection_db import Connection

class TestDeleteTickets:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.ticket_data = TicketFactory.create()

    #Happy Path
    def test_delete_ticket(self):
        self.ticket_data['ID_USER']=1 #Correct Id user
        self.ticket_data['id_ticket'] = 3 # Correct id ticket
        user = int(self.ticket_data['ID_USER'])
        id_ticket = int(self.ticket_data['id_ticket'])
        data = (user, id_ticket)
        message = delete_tickets(user,id_ticket)

        assert message == 'The tickets were eliminated'

        Connection.delete_ticket(data)
    
    #Edge Cases

    def test_the_ticket_does_not_belong_to_the_user(self):
        with pytest.raises(Exception) as error:
            self.ticket_data['ID_USER']=99 #Incorrect ID_USEr
            self.ticket_data['id_ticket'] = 3 #Correct Id_ticket
            user = int(self.ticket_data['ID_USER'])
            id_ticket = int(self.ticket_data['id_ticket'])

            message = delete_tickets(user,id_ticket)

            assert str(error.value) == f'The ticket with id {id_ticket} does not belong to user with id {user}'
    
    def test_the_ticket_has_already_expired(self):
        with pytest.raises(Exception) as error:
            self.ticket_data['ID_USER']=1 #Correct Id user
            self.ticket_data['id_ticket'] = 1 #Correct id ticket 
            user = int(self.ticket_data['ID_USER'])
            id_ticket = int(self.ticket_data['id_ticket'])

            message =  delete_tickets(user,id_ticket)

            assert str(error.value) == f'The ticket with the id {id_ticket} has already expired. You can not delete it.'

