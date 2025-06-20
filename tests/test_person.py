import pytest

from beings import Person

@pytest.fixture()
def person1():
    return Person(name="Andreas Larsen", age=32, hobbies=["Running"])
# @pytest.fixture()
def person2():
    return Person(name="John Doe", age=99)

def test_init(person1):
    assert person1.name == "Andreas Larsen"
    assert person1.age == 32
    assert person1.hobbies == ["Running"]

def test_first_name(person1):
    assert person1.first_name == "Andreas"

def test_last_name(person1):
    assert person1.last_name == "Larsen"

def test_celebrate_birthday(person1):
    initial_age = person1.age
    person1.celebrate_birthday()
    assert person1.age == initial_age + 1

def test_add_hobby(person1):
    initial_hobbies = person1.hobbies.copy()
    new_hobby = "Swimming"
    person1.add_hobby(new_hobby)
    assert new_hobby in person1.hobbies
    assert len(person1.hobbies) == len(initial_hobbies) + 1

