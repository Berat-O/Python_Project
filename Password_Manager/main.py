import csv
import random
import string
from pathlib import Path
from typing import Literal

from rich import box
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

STRING_LENGTH = 6
PUNCTUATION_LENGTH = 4
PASSWORD_FILE = Path("password.csv").resolve()
console = Console()


def display_message(message: str, color: Literal["green", "red", "white", "blue"]) -> None:
    """Display a message in the specified color."""
    console.print(f"[{color}]{message}[/]")


def show_main_menu(last_output: str | None = None) -> int:
    table = Table(
        "[bold]Password Manager App[/]", box=box.SQUARE, caption=last_output, width=50, caption_justify="left"
    )
    table.add_row("1. Create password")
    table.add_row("2. Show password")
    table.add_row("3. Edit password")
    table.add_row("4. Delete password")
    table.add_row("5. Exit")
    console.print(table)

    choice = Prompt.ask(
        "[bold]Select an option[/]", choices=["1", "2", "3", "4", "5"], default="5", show_choices=False, console=console
    )
    return int(choice)


def read_csv_file() -> dict[str, str]:
    """Read the CSV file and return the data as a dict[aim, password]"""
    with PASSWORD_FILE.open("r", encoding="utf-8", newline="") as csvfile:
        return {data[0]: data[1] for data in csv.reader(csvfile) if data}


def write_csv_file(data: dict[str, str]) -> None:
    """Write the data to the CSV file."""
    with PASSWORD_FILE.open("w", encoding="utf-8", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows([[k, v] for k, v in data.items()])


def validate_aim(aim: str) -> bool:
    if not aim or aim in read_csv_file():
        return False
    return True


def password_generator() -> str:
    """Generate a random password with lowercase, uppercase, punctuation, and numeric characters."""
    char_sets = [string.ascii_lowercase, string.ascii_uppercase, string.punctuation, string.digits]
    password = [random.choice(char_set) for char_set in char_sets]
    password.extend(random.choices("".join(char_sets), k=STRING_LENGTH + PUNCTUATION_LENGTH + 4 - len(char_sets)))
    random.shuffle(password)
    return "".join(password)


def process_creation() -> str:
    """Create the password for a given aim in the CSV file."""
    console.clear()
    display_message("Creation mode", "blue")

    if not validate_aim(aim := Prompt.ask("Enter aim", console=console)):
        return "This aim is empty or already taken. Try again"

    data = read_csv_file()
    password = password_generator()
    data[aim] = password
    write_csv_file(data)
    return "Password successfully created"


def process_checking() -> str:
    """Show the password for a given aim in the CSV file."""
    console.clear()
    display_message("Checking mode", "blue")
    data = read_csv_file()

    if not (aim := Prompt.ask("Enter aim", console=console)) or aim not in data:
        return "This aim is empty or not found. Try again"

    password = data.get(aim)
    if password:
        return password
    return "Aim not found"


def process_editing() -> str:
    """Edit the password for a given aim in the CSV file."""
    console.clear()
    display_message("Editing mode", "blue")
    data = read_csv_file()

    if not (aim := Prompt.ask("Enter aim", console=console)) or aim not in data:
        return "This aim is empty or not found. Try again"

    new_password = Prompt.ask("Enter the new password", console=console)
    if new_password != Prompt.ask("Re-enter the new password", console=console):
        return "Passwords do not match. Try again"
    data[aim] = new_password
    write_csv_file(data)
    return "Password updated successfully"


def process_deleting() -> str:
    """Delete a password entry for a given aim from the CSV file."""
    console.clear()
    display_message("Deleting mode", "blue")
    data = read_csv_file()

    if not (aim := Prompt.ask("Enter aim", console=console)) or aim not in data:
        return "This aim is empty or not found. Try again"

    del data[aim]
    write_csv_file(data)
    return "Password removed successfully"


def process_exit() -> None:
    console.clear()
    display_message("Exiting the Password Manager App. Goodbye!", "green")
    exit(0)


def main() -> None:
    last_output = None
    while True:
        console.clear()
        selected = show_main_menu(last_output)
        last_output = None
        match selected:
            case 1:
                last_output = process_creation()
            case 2:
                last_output = process_checking()
            case 3:
                last_output = process_editing()
            case 4:
                last_output = process_deleting()
            case 5:
                process_exit()


if __name__ == "__main__":
    main()
