# Import modules
import random
import string
import csv
import os
from colorama import Fore, Style

# Define constants
STRING_LENGTH = 6
PUNCTUATION_LENGTH = 4
PASSWORD_FILE = "password.csv"

# Define functions


def main():
    while True:
        print("---------------------|")
        print("Password Manager App |")
        print("---------------------|")
        print("1. Create password   |")
        print("2. Check password    |")
        print("3. Edit password     |")
        print("4. Del Password      |")
        print("5. Exit              |")
        print("---------------------|")

        selected = input("Pick a number: ")

        if selected == "1":
            os.system('clear')
            # Ask the user for the aim of the password
            aim = input("Which program use password: ")
            create_password(aim)
        elif selected == "2":
            os.system('clear')
            # Ask the user for the aim of the password
            aim = input("Please type aim to see password: ")
            a = check_password(aim)
            if a == None:
                print(Fore.RED)
                print("----------------------")
                print("Not found")
                print("----------------------")
                print(Style.RESET_ALL)
            else:
                print(Fore.GREEN)
                print("----------------------")
                print(f"Password is :{a}")
                print("----------------------")
                print(Style.RESET_ALL)
        elif selected == "3":
            os.system('clear')
            # Ask the user for the aim of the password
            aim = input(
                "Please enter the aim for which you want to change the password: "
            )
            edit_password(aim)
        elif selected == "4":
            os.system('clear')
            # Ask the user for the aim of the password
            aim = input(
                "Please enter the aim for which you want to delate the password: "
            )
            del_password(aim)
        elif selected == "5":
            print("Exiting the Password Manager App. Goodbye!")
            break
        else:
            print("Invalid option. Please select a valid option (1-5).")


def password_generator() -> str:
    """Generate a random password with lowercase, uppercase, punctuation, and numeric characters."""
    # Create a list of character sets
    char_sets = [
        string.ascii_lowercase,
        string.ascii_uppercase,
        string.punctuation,
        string.digits,
    ]
    # Sample one character from each set and add it to the password list
    password = [random.choice(char_set) for char_set in char_sets]
    # Fill the remaining password length with random characters from all sets
    password.extend(
        random.choices(
            "".join(char_sets),
            k=STRING_LENGTH + PUNCTUATION_LENGTH + 4 - len(char_sets),
        )
    )
    # Shuffle the password list to randomize the order
    random.shuffle(password)
    # Join the password list into a string and return it
    return "".join(password)


def create_password(aim: str) -> str:
    """Create a new password for a given aim and save it to the CSV file."""

    # Check if the aim is valid and not empty
    if aim:
        # Check if the password file exists and create it if not
        if not os.path.isfile(PASSWORD_FILE):
            with open(PASSWORD_FILE, "w", newline="") as csvfile:
                fieldnames = ["aim", "password"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
        # Read the existing aims from the CSV file
        existing_aims = []
        with open(PASSWORD_FILE, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                existing_aims.append(row["aim"])
        # Check if the aim is already used and reject it if so
        if aim in existing_aims:
            print("----------------------------------------------------")
            print("")
            print(Fore.RED + f" '{aim}' is unavailable. Please use a different aim.")
            print(Style.RESET_ALL)
            print("-----------------------------------------------------")
        else:
            # Generate a new password for the aim
            password = password_generator()
            # Append the aim and password to the CSV file
            with open(PASSWORD_FILE, "a", newline="") as csvfile:
                fieldnames = ["aim", "password"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow({"aim": aim, "password": password})
            # Display a success message and the new password
            print("----------------------------------------------")
            print("")
            print(Fore.GREEN + "Password created successfully.")
            print(f"{aim} password is: {password}")
            print(Style.RESET_ALL)
            print("----------------------------------------------")
            return password
    else:
        # Display an error message if the aim is empty
        print("--------------------------------------------------------------")
        print("")
        print(Fore.RED + "Aim unspecified or empty. Please specify an 'aim' value.")
        print(Style.RESET_ALL)
        print("--------------------------------------------------------------")


def check_password(aim: str) -> str:
    """Check the password for a given aim from the CSV file."""

    # Check if the aim is valid and not empty
    if aim:
        # Read the passwords from the CSV file and find the matching one for the aim
        with open(PASSWORD_FILE, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if aim == row["aim"]:
                    return row["password"]


def edit_password(aim: str) -> None:
    """Edit the password for a given aim in the CSV file."""

    # Check if the aim is valid and not empty
    if aim:
        # Read the data from the CSV file and store it in a list
        data = []
        found = False  # To track if the target aim is found
        with open(PASSWORD_FILE, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)
                if aim == row["aim"]:
                    found = True

        # Check if the target aim is found and proceed to edit the password
        if found:
            # Ask the user for the new password and confirm it
            new_password = input("Enter the new password: ")
            confirm_password = input("Re-enter the new password: ")

            # Check if the passwords match and meet the minimum requirements
            if new_password == confirm_password:
                # Update the password for the target aim in the data list
                for row in data:
                    if row["aim"] == aim:
                        row["password"] = new_password

                # Write the updated data back to the CSV file
                with open(PASSWORD_FILE, "w", newline="") as csvfile:
                    fieldnames = ["aim", "password"]
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(data)

                # Display a success message and the new password
                print(f"{Fore.GREEN}Password updated successfully.")
                print(
                    f"{Fore.GREEN}Your new password is {new_password}. {Style.RESET_ALL}"
                )

            else:
                # Display an error message if the passwords do not match or are too short
                print(
                    f"{Fore.RED}Passwords do not match or are too short. Password update failed. {Style.RESET_ALL}"
                )
        else:
            # Display an error message if the target aim is not found
            print(
                f"{Fore.RED}No password found for '{aim}'. Password update failed. {Style.RESET_ALL}"
            )
    else:
        # Display an error message if the aim is empty
        print("--------------------------------------------------------------")
        print("")
        print(Fore.RED + "Aim unspecified or empty. Please specify an 'aim' value.")
        print(Style.RESET_ALL)
        print("--------------------------------------------------------------")


def del_password(aim: str) -> None:
    """Delete a password entry for a given aim from the CSV file."""
    # Check if the aim is valid and not empty
    if aim:
        # Read the data from the CSV file and store it in a list
        data = []
        found = False  # To track if the target aim is found
        with open(PASSWORD_FILE, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if aim == row["aim"]:
                    found = True
                else:
                    data.append(row)

        # Check if the target aim is found and proceed to delete the password entry
        if found:
            # Write the updated data back to the CSV file (excluding the target entry)
            with open(PASSWORD_FILE, "w", newline="") as csvfile:
                fieldnames = ["aim", "password"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data)

            # Display a success message
            print(f"{Fore.GREEN}Password deleted successfully for aim: {aim}")
            print(Style.RESET_ALL)

        else:
            # Display an error message if the target aim is not found
            print(
                f"{Fore.RED}No password found for '{aim}'. Password deletion failed. {Style.RESET_ALL}"
            )
    else:
        # Display an error message if the aim is empty
        print("--------------------------------------------------------------")
        print("")
        print(Fore.RED + "Aim unspecified or empty. Please specify an 'aim' value.")
        print(Style.RESET_ALL)
        print("--------------------------------------------------------------")


if __name__ == "__main__":
    main()
