import re

def check_password_strength(password):
    strength = 0
    remarks = ""

    # Conditions
    if len(password) >= 8:
        strength += 1
    if re.search(r"[a-z]", password):
        strength += 1
    if re.search(r"[A-Z]", password):
        strength += 1
    if re.search(r"\d", password):
        strength += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1

    # Remarks
    if strength <= 2:
        remarks = "Weak"
    elif strength == 3 or strength == 4:
        remarks = "Moderate"
    else:
        remarks = "Strong"

    return remarks

# Input
password = input("Enter your password to check strength: ")
strength = check_password_strength(password)
print(f"Password Strength: {strength}")
