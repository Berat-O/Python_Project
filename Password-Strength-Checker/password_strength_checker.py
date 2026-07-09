def check_password_strength(password):
    strength = 0

    if len(password) >= 8:
        strength += 1

    if any(char.isupper() for char in password):
        strength += 1

    if any(char.islower() for char in password):
        strength += 1

    if any(char.isdigit() for char in password):
        strength += 1

    if any(char in "!@#$%^&*()_+-=[]{}|;:,.<>?/`~" for char in password):
        strength += 1

    if strength <= 2:
        return "Weak Password"
    elif strength <= 4:
        return "Moderate Password"
    else:
        return "Strong Password"


password = input("Enter Password: ")
result = check_password_strength(password)
print("Password Strength:", result)
