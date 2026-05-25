import os


def clear_screen():
    # Clears terminal on Windows, Mac, or Linux
    os.system("cls" if os.name == "nt" else "clear")