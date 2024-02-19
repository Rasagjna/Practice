import sys

import pytest


# @pytest.mark.smoke
# def test_login():
#     print("login to application")
#
# @pytest.mark.regression
# def test_addProduct():
#     print("checkout")
#
# @pytest.mark.smoke
# def test_logout():
#     print("logged out")

@pytest.mark.skip
def test_login():
    print("login to application")


@pytest.mark.skipif(sys.version_info < (3, 11), reason="Python version not supported")
def test_addproducts():
    print("checkout")

@pytest.mark.xfail
def test_logout():
    assert False
    print("logged out")
def test_closeApplication():
    assert True
    print("close the application")

