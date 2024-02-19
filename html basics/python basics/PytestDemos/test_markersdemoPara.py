import sys

import pytest
@pytest.mark.parametrize("username,password",
                         [
                             ("Selenium","WebDriver"),
                             ("Python","Pytest"),
                             ("Mukesh","Otwani"),
                             ("RestAPI","Web")
                         ])
def test_login(username,password):
    print(username)
    print(password)