from src.section_dataclasses import Person


def test_dataclass():
    """
    SPECIFICATION: the dataclass shall save the given values

    ASSUMPTION: the test is correct
    TASK: explain why the test is failing
    """
    person = Person(name="John", age=30, hobbies=["reading", "gaming"])
    assert person.name == "John"
    assert person.nickname is None

    person.hobbies.append("writing")
    assert len(person.hobbies) == 3

    person.age = 2
    assert person.age == 2
