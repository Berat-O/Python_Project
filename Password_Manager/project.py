import random
import string
import os
import time
import sqlite3
import hashlib
from colorama import Fore, Style

STRING_LENGTH = 6
PUNCTUATION_LENGTH = 4
DB_FILE = "passwords.db"

def get_db_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.execute('''
        CREATE TABLE IF NOT EXISTS passwords (
            aim TEXT PRIMARY KEY,
            password_hash TEXT NOT NULL
        )
    ''')
    return conn

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def read_db():
    conn = get_db_connection()
    cursor = conn.execute("SELECT aim, password_hash FROM passwords")
    data = [{"aim": row[0], "password": row[1]} for row in cursor.fetchall()]
    conn.close()
    return data

def write_db(aim, password_hash):
    conn = get_db_connection()
    conn.execute("INSERT INTO passwords (aim, password_hash) VALUES (?, ?)", (aim, password_hash))
    conn.commit()
    conn.close()

def update_db(aim, password_hash):
    conn = get_db_connection()
    conn.execute("UPDATE passwords SET password_hash = ? WHERE aim = ?", (password_hash, aim))
    conn.commit()
    conn.close()

def delete_db(aim):
    conn = get_db_connection()
    conn.execute("DELETE FROM passwords WHERE aim = ?", (aim,))
    conn.commit()
    conn.close()

def password_generator():
    char_sets = [string.ascii_lowercase, string.ascii_uppercase, string.punctuation, string.digits]
    password = [random.choice(char_set) for char_set in char_sets]
    password.extend(random.choices("".join(char_sets), k=STRING_LENGTH + PUNCTUATION_LENGTH + 4 - len(char_sets)))
    random.shuffle(password)
    return "".join(password)

def display_message(message, color=Fore.GREEN):
    print(color + message + Style.RESET_ALL)
    time.sleep(2)

def create_password(aim):
    if not validate_aim(aim):
        return
    data = read_db()
    if aim in [row["aim"] for row in data]:
        display_message(f"'{aim}' is unavailable. Please use a different aim.", Fore.RED)
        return
    password = password_generator()
    password_hash = hash_password(password)
    write_db(aim, password_hash)
    display_message(f"Password created successfully.\n{aim} password is: {password}")

def check_password(aim):
    if not validate_aim(aim):
        return None
    conn = get_db_connection()
    cursor = conn.execute("SELECT password_hash FROM passwords WHERE aim = ?", (aim,))
    row = cursor.fetchone()
    conn.close()
    if row:
        display_message("Password hash is: " + row[0])
        return row[0]
    display_message("No password found for the specified aim.", Fore.RED)
    return None

def edit_password(aim):
    if not validate_aim(aim):
        return
    conn = get_db_connection()
    cursor = conn.execute("SELECT aim FROM passwords WHERE aim = ?", (aim,))
    if not cursor.fetchone():
        display_message(f"No password found for '{aim}'.", Fore.RED)
        conn.close()
        return
    new_password = input("Enter the new password: ")
    if new_password != input("Re-enter the new password: "):
        display_message("Passwords do not match. Password update failed.", Fore.RED)
        conn.close()
        return
    password_hash = hash_password(new_password)
    update_db(aim, password_hash)
    display_message(f"Password updated successfully.\nYour new password is {new_password}.")
    conn.close()

def del_password(aim):
    if not validate_aim(aim):
        return
    data = read_db()
    if aim not in [row["aim"] for row in data]:
        display_message(f"No password found for '{aim}'.", Fore.RED)
        return
    delete_db(aim)
    display_message(f"Password deleted successfully for aim: {aim}")

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

def main():
    while True:
        os.system('clear')
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
                password = check_password(aim)
                if password:
                    display_message(f"Password is: {password}")
            elif selected == "3":
                edit_password(aim)
            elif selected == "4":
                del_password(aim)
        else:
            display_message("Invalid option. Please select a valid option (1-5).", Fore.RED)

if __name__ == "__main__":
    main()
