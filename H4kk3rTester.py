from H4kk3r import rules
import pytest

def TestValidPassword():
    assert rules ("Passw0rd") == []
def TestMissingP():
    assert rules ("assw0rd")
def TestMissingD():
    assert rules ("Passw0rb")
def Testmissingint():
    assert rules ("Password")
def Testnocaps():
    assert rules ("passw0rd")