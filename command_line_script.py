#!/usr/bin/env python3
import os
import typer
from typing import Optional
from Simulator import Type
import time


def autotype_cli(
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
):
    """
    A quick and small python script that helps you autotype on websites that have copy paste disabled like Moodle, HackerEarth contests etc as it is difficult to efficiently debug your code on an online compiler.

    --path: the path to the file.

    --delay: time delay before typing.

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
        total = 0
        with typer.progressbar(
            range(100),
            label=typer.style(
                "Writing File in Progress -> ", fg=typer.colors.GREEN, bold=True
            ),
        ) as progress:
            for value in progress:
                time.sleep(0.01)
                total += 1
        Type(path, delay)
        successfull_file_path = typer.style(
            f"{path} File", fg=typer.colors.BRIGHT_GREEN
        )
        time_taken = typer.style(
            f"is written in {abs(delay)} seconds", fg=typer.colors.BRIGHT_WHITE
        )
        typer.echo(f"{successfull_file_path + ' ' + time_taken}")


if __name__ == "__main__":
    typer.run(autotype_cli)
