# 🔐 Password Manager

## 📌 Description

This is a simple **command-line Password Manager application** built with **Python**.
It allows users to:

* Create and store passwords for a specific purpose (website, app, or account)
* Check saved passwords
* Edit existing passwords
* Delete passwords
* Store password records in a CSV file

> ⚠️ This project is intended for **learning and basic utility purposes**.

---

## 🚀 Getting Started

Follow these steps to run the project locally.

### 1) Clone the repository

```bash
git clone <repository-url>
cd Python_Project/Password_Manager
```

### 2) Install requirements

```bash
pip install colorama
```

### 3) Run the project

```bash
python project.py
```

---

## 🧑‍💻 Features

The Password Manager provides the following options:

* **Create Password** → Generate and save a password for a specific aim
* **Check Password** → View the password for a saved aim
* **Edit Password** → Update the password of an existing entry
* **Delete Password** → Remove a password entry
* **Exit** → Close the application

---

## 📖 Usage Guide

### ➕ Create a Password

Choose **Option 1** and enter the purpose (for example: website, email, or app).
The application generates a password and saves it in the CSV file.

### 🔍 Check a Password

Choose **Option 2** and enter the saved purpose.
The application displays the corresponding password if it exists.

### ✏️ Edit a Password

Choose **Option 3** and enter the purpose.
Then provide a new password to update the existing record.

### 🗑️ Delete a Password

Choose **Option 4** and enter the purpose.
The password record will be removed.

### ❌ Exit

Choose **Option 5** to safely exit the application.

---

## 📂 Data Storage

All passwords are stored in:

```text
password.csv
```

This file is located in the same directory as `project.py`.

---

## ⚠️ Security Notice

This password manager stores passwords in a **plain CSV file**, which means the data is **not encrypted**.

Please note:

* Do **not** use this project for real sensitive passwords
* Keep `password.csv` secure
* Use it mainly for **learning and practice purposes**

---

## 🛠️ Tech Stack

* Python 3
* CSV file handling
* Colorama

---

## 🤝 Contribution

Contributions are welcome!
You can improve:

* README documentation
* code readability
* encryption support
* password strength checks
* error handling
* CSV structure

Happy coding 🚀
