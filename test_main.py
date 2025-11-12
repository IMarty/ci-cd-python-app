import datetime
import main
from unittest.mock import patch, MagicMock

@patch('datetime.datetime')
def test_greet_hello(MockDateTime):
    # Create a mock object for the return value of datetime.datetime.now()
    mock_now = MagicMock()
    
    # Configure the hour property of the mock object to return the integer 10
    mock_now.hour = 10 
    
    # Configure the mocked datetime.datetime.now() to return the mock object
    MockDateTime.now.return_value = mock_now 
    
    # Now, main.get_greeting() will see the hour as the integer 10
    assert main.get_greeting() == "Hello"