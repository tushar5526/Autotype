from pynput.keyboard import Key, Controller
from time import sleep
from dataclasses import dataclass


@dataclass
class Autotype:
    """

    """
    default_delay: int = 3
    default_code: str = """
class Main:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"The name is {self.name} and the age is {self.age{"
"""
    @classmethod
    def type(cls, path: str = None, delay: int = None, code: str = None):
        """
        
        """
        if not delay:
            delay = cls.default_delay

        if delay < 0:
            print()
            delay = abs(cls.default_delay)

        sleep(delay)

        if path:
            with open(path, "r") as File:
                code = File.read()
        elif code:
            pass
        else:
            code = cls.default_code

        keyboard = Controller()
        for line in code.split("\n"):
            keyboard.type(line)
            sleep(0.1)
            keyboard.tap(Key.enter)
            keyboard.tap(Key.home)