def test_1():
    x=18
    y=18
    assert x==y
def test_2():
    name="Selenium"
    title="Selenium is for web automation"
    assert name in title
def test_3():
    name="Jenkins"
    title="Jenkins is CI server"
    assert name in title,"title doesnot match"