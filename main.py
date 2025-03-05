import os
import time
from ip_tracker import ip_track
from show_ip import show_ip
from phone_tracker import phone_gw  # Importing the phone_gw function from phone_tracker.py
from username_tracker import track_username

# Color Definitions
Wh = '\033[1;37m'  # White
Gr = '\033[1;32m'  # Green
Re = '\033[1;31m'  # Red

# Menu Options
options = [
    {'num': 1, 'text': 'IP Tracker', 'func': ip_track},
    {'num': 2, 'text': 'Show Your IP', 'func': show_ip},
    {'num': 3, 'text': 'Phone Number Tracker', 'func': phone_gw},  # Linking phone tracker here
    {'num': 4, 'text': 'Username Tracker', 'func': track_username},
    {'num': 0, 'text': 'Exit', 'func': exit}
]

# Clear Console Screen
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Display Menu Options
def option_text():
    text = f"{Wh}========== MENU ==========\n"
    for opt in options:
        text += f"[ {opt['num']} ] {Gr}{opt['text']}\n"
    return text

# Check if the option exists in the menu
def is_in_options(num):
    return any(opt['num'] == num for opt in options)

# Execute the Selected Option
def execute_option(opt):
    for option in options:
        if option['num'] == opt:
            option['func']()  # Call the associated function

# Main Menu Loop
def main():
    while True:
        try:
            clear()
            print(option_text())
            choice = input(f"{Wh}Choose an option: {Gr}")
            
            # Validate input
            if choice.isdigit():
                choice = int(choice)
                if is_in_options(choice):
                    execute_option(choice)
                    input(f'\n{Wh}[ {Gr}+ {Wh}] {Gr}Press Enter to continue...')
                else:
                    print(f"{Re}Invalid option! Please choose a valid number.")
            else:
                print(f"{Re}Invalid input! Please enter a number.")
            time.sleep(1)

        except KeyboardInterrupt:
            print(f'\n{Wh}[ {Re}! {Wh}] {Re}Exit')
            time.sleep(1)
            exit()

# Run the Program
if __name__ == "__main__":
    main()
