import pyautogui as root
import time
import pyperclip
import random


def get_text():
    # take lines from a file
    count = random.choice(range(0, 10))
    with open('invites.txt', 'r', encoding="latin-1") as f:
        lines = f.readlines()
        first_line = lines[count]
        pyperclip.copy(first_line)


def get_data(To_browser, To_place, To_button):
    try:
        # Goes to browser x, y
        root.moveTo(To_browser, duration=0.5)
        root.click()

        # Inserts text into an input field x, y
        root.moveTo(To_place, duration=0.5)
        root.click()
        root.hotkey("ctrl", "v")

        # Moves to button invite x, y
        root.moveTo(To_button, duration=0.5)
        root.click()
    except Exception as r:
        print(r)


def send_invites():
    # Stable coordinates x, y
    entry_field = "int, int"
    button = "int, int"
    while True:
        time.sleep(15)
        try:
            # Insert your x, y in Run
            Run = "int, int"
            get_text()
            get_data(To_browser=Run, To_place=entry_field, To_button=button)

            time.sleep(5)
            Run2 = "int, int"
            get_text()
            get_data(To_browser=Run2, To_place=entry_field, To_button=button)

        except Exception as d:
            print(d)


if __name__ == "__main__":
    send_invites()