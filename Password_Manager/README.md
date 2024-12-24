 # Password Manager

#### Description:

This is a simple command-line password manager app written in Python. It allows you to create, check, edit, and delete passwords associated with specific aims (e.g., program names, websites) and stores them in a CSV file.

# Getting Started

To use this password manager, follow these steps:

1. Clone or download this repository to your local machine.
2. Make sure you have Python 3.x installed.
3. Install the required libraries by running the following command in your terminal or command prompt:
    ```bash
    pip install colorama
4. Run the password_manager.py script:
    ```bash
    python password_manager.py

# Usage

The Password Manager App provides the following options:

**Create Password:** Allows you to generate and save a new password for a specific aim (e.g., program or website).
**Check Password:** Allows you to check and display a password associated with a specific aim.
**Edit Password:** Allows you to change the password for a specific aim.
**Delete Password:** Allows you to delete a password entry for a specific aim.
**Exit:** Allows you to exit the Password Manager App.

# Creating a Password
To create a password for a specific aim, choose option 1, and then enter the aim (e.g., program or website) for which you want to create a password. The app will generate a random password for you and display it. Make sure to save this password in a safe place since it will not be retrievable again.

# Checking a Password
To check a password associated with a specific aim, choose option 2, and then enter the aim. The app will display the password if it exists in the database.

# Editing a Password
To change the password associated with a specific aim, choose option 3, and then enter the aim. You will be prompted to enter a new password, and it will be updated in the database.

# Deleting a Password
To delete a password entry for a specific aim, choose option 4, and then enter the aim. The password associated with that aim will be deleted from the database.

# Exiting the App
To exit the Password Manager App, choose option 5.

# CSV File

The app stores password information in a CSV file named password.csv in the same directory as the script. You can manually edit this file if needed.

# Security Notice

This Password Manager App is a simple utility for managing passwords and does not provide advanced security features. As the CSV file containing passwords is not encrypted, it's essential to keep it secure.






