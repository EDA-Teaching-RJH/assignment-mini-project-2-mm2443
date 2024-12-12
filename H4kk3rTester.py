# this section validates the password puzzle is all correct and all of the rules will work before the user starts the program
from H4kk3r import validate_password

def test_ValidPassword(): # this one tests a correct answer to see if it does let the user through to the next section 
    assert validate_password("Passw0rd") == []

def test_MissingP(): # this one tests to make sure an error comes up and gives the user a hint that they need to use a letter p
    assert "Password must start with 'p'" in validate_password("assw0rd")

def test_MissingD(): #this one tests to make sure an error comes up and gives the user a hint that they need to use a letter d
    assert "Password must end with 'd'" in validate_password("Passw0rb")

def test_MissingInt(): # this one tests to make sure an error comes up and gives the user a hint that they need to use a number
    assert "Password must contain at least one digit" in validate_password("Password")

def test_NoCaps(): # this one makes sure that there is at least one capital letter within the program
    assert "Password must include an uppercase letter" in validate_password("passw0rd")