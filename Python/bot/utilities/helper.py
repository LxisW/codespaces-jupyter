import colorama
import os
from datetime import datetime


class Helper:
    def __init__(self) -> None:
        pass

    @staticmethod
    def colored_text(text: str, color: str):
        # creates colored text
        colorama.init()
        color_dict = {
            "red": colorama.Fore.RED,
            "green": colorama.Fore.GREEN,
            "blue": colorama.Fore.BLUE,
            "yellow": colorama.Fore.YELLOW,
            "magenta": colorama.Fore.MAGENTA,
            "cyan": colorama.Fore.CYAN,
            "white": colorama.Fore.WHITE,
            "orange": "\033[38;2;255;165;0m",  # RGB for orange
            "reset": colorama.Fore.RESET
        }
        selected_color = color_dict.get(color.lower(), colorama.Fore.RESET)

        # Print the colored text
        print(
            f"{selected_color}[{datetime.now().strftime('%H:%M:%S.%f')[:-3]}] {text}{colorama.Fore.RESET}")

    @staticmethod
    def clear_console():
        command = "clear"
        if os.name in ("nt", "dos"):
            command = "cls"
        os.system(command)
