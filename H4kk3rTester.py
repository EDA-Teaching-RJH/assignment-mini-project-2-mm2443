from H4kk3r import validate_password

def test_ValidPassword():
    assert validate_password("Passw0rd") == []

def test_MissingP():
    assert "Password must start with 'p'" in validate_password("assw0rd")

def test_MissingD():
    assert "Password must end with 'd'" in validate_password("Passw0rb")

def test_MissingInt():
    assert "Password must contain at least one digit" in validate_password("Password")

def test_NoCaps():
    assert "Password must include an uppercase letter" in validate_password("passw0rd")