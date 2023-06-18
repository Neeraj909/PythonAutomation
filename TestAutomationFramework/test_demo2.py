# Any pytest file should start with test_ or end with _test
#pytest methods name should start with test
#-k stands for method name execution , -s log in out put, -v stands for more info like metadata
# can specific file with py.test with filename
# can mark (tag) tests @pytest.mark.smoke and run with -m
# can skipp test with @pytest.mark.skip
# fixtures are used setup and tear down methods for test cases - conftest file to generalize fixture
# and make it available to all test case
import pytest


def test_firstProgram(setup):
    print("firstProgram")

@pytest.mark.smoke
#@pytest.mark.skip
#@pytest.mark.xfail
def test_secondProgram():
    print("secondProgram")
    msg="hello"
    assert msg in "hi"



