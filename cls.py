import os
def clear_screen():
    os.system("cls") if os.name == "nt" else os.system("clear")

if __name__ == "__main__":
    clear_screen()