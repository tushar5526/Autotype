from .core import Autotype
from .gui import App
import typer
import os


def main(cli: bool = True, gui: bool = False) -> None:
    """
                A quick and small python script that helps you autotype on websites that have copy paste disabled like Moodle, HackerEarth contests etc as it is difficult to efficiently debug your code on an online compiler.

                --cli --no-gui: for CLI

                --gui --no-cli: for GUI

    """
    if cli:
        path: str = input("path: 🗂️ - ")
        delay: int = int(input("delay: ⏰ - "))
        if os.path.exists(path):
            Autotype().type(path=path, delay=delay)
        else:
            print("Path Not Found")
    if gui:
        app = App()
        app.start()


typer.run(main)
