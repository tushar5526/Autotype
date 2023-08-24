from pynput.keyboard import Key, Controller
from time import sleep


def Type(
    path: str = None,
    delay: int = 3,
    code: str = None,
    key_delay: float = 0.1,
    line_delay: float = 0.1,
):
    # If Any of the delay is negative
    if delay < 0 or key_delay < 0 or line_delay < 0:
        print("Hmmmmmmmmm 😱 Interesting Time is negative 🥲")
        delay = abs(delay)
        key_delay = abs(key_delay)
        line_delay = abs(line_delay)

    # wait for few seconds before typing
    sleep(delay)

    # manually enter your code here or provide a path
    if path:
        with open(path, "r") as file:
            code = file.read()
    elif code:
        pass
    else:
        code = """
    class Complex:
        def __init__(self, x, y):
            self.x = x
            self.y = y
        """

    keyboard = Controller()
    for line in code.split("\n"):
        for char in line:
            keyboard.type(char)
            sleep(key_delay)  # Add a key_delay seconds between each keystroke
        keyboard.tap(Key.enter)
        keyboard.tap(Key.home)
        sleep(line_delay)  # Add a line_delay seconds between each line
