from movies import requestMovies
import pytest

class TestRequestMovies:
     #Happy Path
    def test_request_movies(self):

        message = requestMovies()

        assert message ==  'Here are the available movies and their functions'
    
    #Edge case
    def test_no_movies_available(self):
        with pytest.raises(Exception) as error:
            message = requestMovies()

            assert str(error.value) == 'No movies available.'