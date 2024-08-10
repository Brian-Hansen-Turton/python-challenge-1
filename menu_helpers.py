import os
import platform

def clear_console():
    # Check if the operating system is Windows
    if platform.system() == "Windows":
        os.system("cls")
    else:
        # If not Windows, assume it's a Unix-like system (Linux, macOS, etc.)
        os.system("clear")
