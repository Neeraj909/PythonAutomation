# Any pytest file should start with test_ or end with _test
#pytest methods name should start with test
#-k stands for method name execution , -s log in out put, -v stands for more info like metadata
# can specific file with py.test with filename
import pytest


@pytest.mark.smoke
def test_firstTest(setup):
    print("First")

def test_secondTest():
    print("Second")
