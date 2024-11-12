import random
import string
import csv
import os
import time
from colorama import Fore, Style
import hashlib
import bcrypt

STRING_LENGTH = 6
PUNCTUATION_LENGTH = 4
PASSWORD_FILE = "password.csv"


def main_menu():
    """Display the main menu and get the user's choice."""
    menu = [
        "---------------------|",
        "Password Manager App |",
        "---------------------|",
        "1. Create password   |",
        "2. Check password    |",
        "3. Edit password     |",
        "4. Delete password   |",
        "5. Exit              |",
        "---------------------|"
    ]
    print("\n".join(menu))
    return input("Pick a number: ")


def validate_aim(aim):
    """Validate if the aim is not empty."""
    if not aim:
        display_message("Aim unspecified or empty. Please specify an 'aim' value.", Fore.RED)
        return False
    return True


def read_csv_file():
    """Read the CSV file and return the data as a list of dictionaries."""
    if not os.path.isfile(PASSWORD_FILE):
        return []
    with open(PASSWORD_FILE, "r") as csvfile:
        return list(csv.DictReader(csvfile))


def write_csv_file(data):
    """Write the data to the CSV file."""
    with open(PASSWORD_FILE, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["aim", "password"])
        writer.writeheader()
        writer.writerows(data)


def password_generator():
    """Generate a random password with lowercase, uppercase, punctuation, and numeric characters."""
    char_sets = [string.ascii_lowercase, string.ascii_uppercase, string.punctuation, string.digits]
    password = [random.choice(char_set) for char_set in char_sets]
    password.extend(random.choices("".join(char_sets), k=STRING_LENGTH + PUNCTUATION_LENGTH + 4 - len(char_sets)))
    random.shuffle(password)
    return "".join(password)


def display_message(message, color=Fore.GREEN):
    """Display a message in the specified color."""
    print(color + message + Style.RESET_ALL)
    time.sleep(2)


def create_password(aim):
    """Create a new password for a given aim and save it to the CSV file."""
    if not validate_aim(aim):
        return
    data = read_csv_file()

    if aim in [row["aim"] for row in data]:
        display_message(f"'{aim}' is unavailable. Please use a different aim.", Fore.RED)
        return

    password = password_generator()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    data.append({"aim": aim, "password": hashed_password})
    write_csv_file(data)
    display_message(f"Password created successfully.\n{aim} password is: {password}")


def check_password(aim):
    """Check the password for a given aim from the CSV file."""
    if not validate_aim(aim):
        return None
    data = read_csv_file()

    for row in data:
        if aim == row["aim"]:
            return row["password"]
    display_message("No password found for the specified aim.", Fore.RED)
    return None


def edit_password(aim):
    """Edit the password for a given aim in the CSV file."""
    if not validate_aim(aim):
        return
    data = read_csv_file()

    for row in data:
        if aim == row["aim"]:
            new_password = input("Enter the new password: ")
            if new_password != input("Re-enter the new password: "):
                display_message("Passwords do not match. Password update failed.", Fore.RED)
                return

            hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            row["password"] = hashed_password
            write_csv_file(data)
            display_message(f"Password updated successfully.\nYour new password is {new_password}.")
            return

    display_message(f"No password found for '{aim}'.", Fore.RED)


def del_password(aim):
    """Delete a password entry for a given aim from the CSV file."""
    if not validate_aim(aim):
        return
    data = read_csv_file()
    new_data = [row for row in data if row["aim"] != aim]
    if len(new_data) == len(data):
        display_message(f"No password found for '{aim}'.", Fore.RED)
        return
    write_csv_file(new_data)
    display_message(f"Password deleted successfully for aim: {aim}")


def main():
    while True:
        os.system('clear')  # clear the screen (or 'cls' for Windows)
        selected = main_menu()

        if selected == "5":
            display_message("Exiting the Password Manager App. Goodbye!")
            break

        if selected in "1234":
            os.system('clear')
            aim = input("Enter aim: ")

            if selected == "1":
                create_password(aim)
            elif selected == "2":
                hashed_password = check_password(aim)
                if hashed_password:
                    display_message(f"Password found for '{aim}'. (hashed)", Fore.CYAN)  # Note: show hashed password
            elif selected == "3":
                edit_password(aim)
            elif selected == "4":
                del_password(aim)
        else:
            display_message("Invalid option. Please select a valid option (1-5).", Fore.RED)


if __name__ == "__main__":
    main()
