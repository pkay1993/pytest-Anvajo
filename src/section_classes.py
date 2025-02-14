import logging
import random

LOGGER = logging.getLogger(__name__)

class Animal:
    def __init__(self, name: str):
        self.name = name
        LOGGER.info("Initialized Animal")

    def make_sound(self) -> str:
        LOGGER.info("Making Animal sound")
        return "Any sound!"

    def make_move(self):
        raise NotImplementedError()

class Dog(Animal):
    def bark(self) -> str:
        LOGGER.info("Making Dog sound")
        return "A dog sound!"

    def run(self) -> str:
        LOGGER.info("Dog running")
        return "Running!"
    
    def make_move(self) -> str:
        return "Running!"
    
    def make_sound(self) -> str:
        return "A dog sound!"
    


class Cat(Animal):
    _hungry = None

    @property
    def hungry(self) -> bool:
        if self._hungry is None:
            self._hungry = random.choice([True, False])
            LOGGER.debug("Cat is hunge=%s", self._hungry)
        return self._hungry

class Horse(Animal):
    """horse class"""
    def __init__(self, name: str, height : str):
        super().__init__(name)
        self.height = height
    # TASK: add implementation here
