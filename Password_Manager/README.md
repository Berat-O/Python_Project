# 🔐 Password Manager - Documentation

This is a command-line based **Password Manager** written in Python. It allows you to securely generate, store, retrieve, edit, and delete passwords for different "aims" (e.g., websites, applications, services). Passwords are encrypted using a symmetric key with the help of the `cryptography` library.

---

## 🧠 Features

- ✅ Generate strong, random passwords
- 🔐 Encrypt passwords using Fernet symmetric encryption
- 🧾 Store passwords in a local SQLite database
- 🔍 Retrieve and view stored passwords
- ✏️ Update existing passwords
- ❌ Delete passwords when no longer needed
- 🗝️ Use a persistent master key stored in `master.key`

---

## 🗂️ File Structure

| File         | Purpose                                                |
|--------------|--------------------------------------------------------|
| `passwords.db` | Stores encrypted passwords in SQLite                 |
| `master.key`   | Contains the symmetric encryption key (Fernet)       |
| main script    | Contains all password manager logic and UI           |

---

## 🔐 Master Key (`master.key`)

The program uses a **master encryption key** to protect your passwords. This key is created or loaded at runtime and stored in a file named `master.key`.

### How it works:

```python
def load_or_create_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)
    else:
        with open(KEY_FILE, "rb") as f:
            key = f.read()
    return key
```

- If `master.key` does not exist, a new key is generated and saved.
- If it exists, it's read from disk.
- The key is then used by the `Fernet` object for encryption/decryption.

> ⚠️ **If `master.key` is deleted or modified, all stored passwords will become unreadable.**

---

## 🔧 Core Functions

### Password Generation

```python
def password_generator():
    ...
```

- Uses a mix of lowercase, uppercase, digits, and punctuation
- Random and strong: ensures complexity and uniqueness

---

### Create Password

```python
def create_password(aim, fernet):
    ...
```

- Validates the aim
- Checks if the aim already exists
- Generates and encrypts a password
- Saves it to the database

---

### Retrieve Password

```python
def check_password(aim, fernet):
    ...
```

- Finds the encrypted password for the aim
- Decrypts and returns it using Fernet

---

### Edit Password

```python
def edit_password(aim, fernet):
    ...
```

- Confirms aim exists
- Prompts for a new password
- Updates the database with the new encrypted password

---

### Delete Password

```python
def del_password(aim):
    ...
```

- Checks if the aim exists
- Deletes it from the database

---

## 🧾 Database Structure

The database (`passwords.db`) uses SQLite and contains a single table:

```sql
CREATE TABLE IF NOT EXISTS passwords (
    aim TEXT PRIMARY KEY,
    password_encrypted TEXT NOT NULL
)
```

- `aim`: A string identifier (e.g., website name)
- `password_encrypted`: The password encrypted with Fernet

---

## 🎨 Terminal Output

- Uses `colorama` to color output messages for better readability
- Displays error/success/status messages in red, green, etc.

---

## 🛡️ Security Best Practices

| Aspect         | Recommendation                                                  |
|----------------|-----------------------------------------------------------------|
| `master.key`   | Keep this file private and secure                               |
| Backup         | Back up `master.key` securely — losing it means lost access     |
| Access         | Do not share or expose the folder where the app runs            |
| Terminal use   | Run only on trusted systems to avoid keylogging or tampering    |

---

## ✅ Summary

| Component        | Role                                                   |
|------------------|--------------------------------------------------------|
| `master.key`     | Stores symmetric encryption key used by `Fernet`       |
| `passwords.db`   | Stores encrypted passwords with their associated aims  |
| `Fernet`         | Handles encryption and decryption                      |
| `colorama`       | Enhances readability of terminal messages              |
| SQLite           | Lightweight embedded database for storing credentials  |

> 🧠 Treat `master.key` as your vault's real key. If lost or exposed, your data is at risk.

---

## 🚀 How to Use

1. Run the script: `python your_script.py`
2. Choose an option from the menu:
   - Create, check, edit, or delete a password
3. Enter an "aim" (e.g., `github`, `email`, `netflix`)
4. Follow the instructions shown in the terminal

Passwords are encrypted, securely stored, and only accessible with the same `master.key`.

```bash
---------------------|
Password Manager App |
---------------------|
1. Create password   |
2. Check password    |
3. Edit password     |
4. Delete password   |
5. Exit              |
---------------------|
```

Enjoy secure, local password management!
