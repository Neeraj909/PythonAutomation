import pytest

@pytest.mark.usefixtures("setup")
class TestFixtureExample:

    def test_fourProgram(self):
        print("depends on fixture method ")

    def test_fourProgramOne(self):
        print("depends on fixture method One ")

    def test_fourProgramTwo(self):
        print("depends on fixture method Two ")

    def test_fourProgramThree(self):
        print("depends on fixture method Three ")

    def test_fourProgramFour(self):
        print("depends on fixture method  Four")
