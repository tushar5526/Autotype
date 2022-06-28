from pynput.keyboard import Key, Controller
from time import sleep


def Type(path=None, delay=None):
    if not delay:
        delay = 3

    # wait for few seconds before typing
    sleep(delay)

    # manually enter your code here or provide a path
    code = """
class Complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    """
    if path:
        with open(path, 'r') as file:
            code = file.read()

    keyboard = Controller()
    for line in code.split('\n'):
        keyboard.type(line)
        keyboard.tap(Key.enter)
        keyboard.tap(Key.home)