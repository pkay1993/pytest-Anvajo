import pytest

from src.section_classes import Animal, Cat, Dog, Horse


def test_inheritance():
    """
    SPECIFICATION: 'Animal' and 'Dog' are inherited

    TASK: patch the implementation to match the the assertions
    """
    animal = Animal("Generic Animal")
    dog = Dog("Rover")

    assert isinstance(dog, Animal)
    assert animal.make_sound() == "Any sound!"
    assert dog.bark() == "A dog sound!"

    with pytest.raises(NotImplementedError):
        animal.make_move()

    assert dog.run() == "Running!"
    assert dog.make_move() == "Running!"
    assert dog.make_sound() == "A dog sound!"

def test_properties():
    """
    ASSUMPTION: test is correct, implementation is correct
    TASK: explain how 'hungry' is implemented
    HINT: Why does the use of 'random' not change the attribute on each call?
    """
    cat = Cat("Garfield")
    state_1 = cat.hungry
    assert state_1 in [True, False]

    state_2 = cat.hungry
    assert state_2 in [True, False]

    assert state_1 == state_2
    # pytest.fail("Remove this when you got an explanation.")
    # hungry wird einmal gesetzt und ist dann nicht mehr none also wird es nicht neu zugeordnet


def test_horse():
    """
    SPECIFICATION: 'Horse' should have another attribute for 'height'

    ASSUMPTION: test is correct
    TASK: patch the implementation
    """
    horse = Horse("Bella", 136)
    assert horse.name == "Bella"
    assert horse.height == 136
