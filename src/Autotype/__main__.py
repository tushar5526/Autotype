#!/usr/bin/env python3
import os
import typer
from typing import Optional
from Autotype.simulate_keyboard import Type
from Autotype import __version__
import time

app = typer.Typer()


@app.command()
def version():
    """
    Check the Version of Autotype 🖊️
    """
    print(f"Autotype {__version__} 🖊️")


@app.command()
def type(
    path: Optional[str] = typer.Option(
        default="",
        help=typer.style("the path to the file 🗂", fg=typer.colors.MAGENTA),
        prompt=True,
        confirmation_prompt=True,
        show_default="Empty File Path",
    ),
    delay: Optional[int] = typer.Option(
        default=3,
        help=typer.style(
            "time ⌛️ delay before typing (in seconds)", fg=typer.colors.MAGENTA
        ),
        show_default=3,
        prompt=True,
    ),
    key_delay: Optional[int] = typer.Option(
        default=0.1,
        help=typer.style(
            "Delay ⏳ in Seconds Between Each keystroke 🎹", fg=typer.colors.MAGENTA
        ),
        show_default=0.1,
    ),
    line_delay: Optional[int] = typer.Option(
        default=0.1,
        help=typer.style(
            "Delay ⏳ in Seconds Between Each line 📈", fg=typer.colors.MAGENTA
        ),
        show_default=0.1,
    ),
):
    """
    A quick and small python script that helps you autotype on websites that have copy paste disabled like Moodle, HackerEarth contests etc as it is difficult to efficiently debug your code on an online compiler.

    --path: the path to the file.

    --delay: time delay before typing.

    --key_delay: key_delay seconds between each keystroke

    --line_delay: line_delay seconds between each line

    return: Prints the File Given.
    """
    if path and not os.path.isfile(path):
        file_path = typer.style(
            f"{path}",
            fg=typer.colors.BRIGHT_WHITE,
            bg=typer.colors.BRIGHT_RED,
            bold=True,
        )
        error_message = typer.style(
            "is not found Please Specify the correct Path.", fg=typer.colors.RED
        )
        typer.echo(f"{file_path + ' ' + error_message} ")
        raise typer.Exit(code=0)
    else:
        Type(path=path, delay=delay, key_delay=key_delay, line_delay=line_delay)
        successfull_file_path = typer.style(
            f"{path} File", fg=typer.colors.BRIGHT_GREEN
        )
        time_taken = typer.style(
            f"is written in {abs(delay)} seconds", fg=typer.colors.BRIGHT_WHITE
        )
        typer.echo(f"{successfull_file_path + ' ' + time_taken}")


if __name__ == "__main__":
    app()
