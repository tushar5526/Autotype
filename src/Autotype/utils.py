import time
import progressbar
from colorama import Fore, Style, init

init(autoreset=True)  # Initialize colorama


def progress_bar(total_time):
    widgets = [
        "Progress: ",
        progressbar.Percentage(),
        " ",
        Fore.GREEN,
        progressbar.Bar(marker="█"),
        " ",
        progressbar.Timer(),
        " ",
        progressbar.ETA(),
        Style.RESET_ALL,
    ]

    with progressbar.ProgressBar(widgets=widgets, max_value=total_time) as bar:
        for i in range(total_time):
            time.sleep(1)
            bar.update(i + 1)

    print(Fore.CYAN + "Progress complete!" + Style.RESET_ALL)
