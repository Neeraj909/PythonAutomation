import pytest


@pytest.fixture(scope="class")
def setup():
    print("priority based test case")
    yield
    print("this is like after method")