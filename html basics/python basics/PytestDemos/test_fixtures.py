import pytest

@pytest.fixture
def setup():
    print("start browser")
    # driver = webdriver.Chrome(ChromeDriverManager().install())

    yield
    print("close browser")
def test_1(setup):
    # print("start browser")
    print("test 1 executed")
    # print("close browser")
def test_2(setup):
    # print("start browser")
    print("test 1 executed")
    # print("close browser")

def test_3(setup):
    # print("start browser")
    print("test 1 executed")
    # print("close browser")
