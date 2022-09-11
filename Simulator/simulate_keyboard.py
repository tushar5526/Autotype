from pynput.keyboard import Key, Controller
from time import sleep


def Type(path: str = None, delay: int = None):
    # If the Argument is negative
    if not delay:
        delay = 3

    if delay < 0:
        print("Hmmmmmmmmm 😱 Interesting Time is negative 🥲")
        delay = abs(delay)

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
        with open(path, "r") as file:
            code = file.read()

    keyboard = Controller()
    for line in code.split("\n"):
        keyboard.type(line)
        # It was observed that a small sleep in between each lines, makes Autotype perform better
        sleep(0.1)
        keyboard.tap(Key.enter)
        keyboard.tap(Key.home)
