from pynput.keyboard import Key, Controller
from time import sleep
from dataclasses import dataclass


@dataclass
class Autotype:
    default_delay: int = 3
    default_code: str = """
    class Complex:
        def __init__(self, x, y):
            self.x = x
            self.y = y
    """

    # def __init__(self, path: str = None, delay: int = None, code: str = None):
    #     self.path = path
    #     self.delay = delay
    #     self.code = code

    def type(self, path: str = None, delay: int = None, code: str = None):
        if not delay:
            delay = self.default_delay

        if delay < 0:
            print()
            delay = abs(self.default_delay)

        sleep(delay)

        if path:
            with open(path, "r") as File:
                code = File.read()
        elif code:
            pass
        else:
            code = self.default_code

        keyboard = Controller()
        for line in code.split("\n"):
            keyboard.type(line)
            sleep(0.1)
            keyboard.tap(Key.enter)
            keyboard.tap(Key.home)