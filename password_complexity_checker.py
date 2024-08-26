import re
import getpass

print("--- Welcome to the Password Strength Checker! ---")

def evaluate_password_strength(password):
    # Check if the password meets various criteria
    has_numbers = any(char.isdigit() for char in password)
    has_upper_and_lower = any(char.isupper() or char.islower() for char in password)
    is_long_enough = len(password) >= 8
    has_special_chars = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    # Count how many criteria are satisfied
    criteria_met = sum([has_numbers, has_upper_and_lower, is_long_enough, has_special_chars])

    # Determine the strength of the password based on the criteria met
    if criteria_met == 4:
        return "Very Strong: Your password meets all the requirements!"
    elif criteria_met == 3:
        return "Moderately Strong: Your password meets three out of four criteria."
    elif criteria_met == 2:
        return "Strong: Your password meets two out of four criteria."
    else:
        return "Weak: Your password meets one or none of the criteria."

# Prompt user to enter their password securely
password = getpass.getpass("Please enter your password: ")

# Mask the password for display purposes
masked_password = password[0] + '#' * (len(password) - 2) + password[-1]

# Evaluate the password strength
strength_message = evaluate_password_strength(password)

# Show the user their password in a masked format along with the strength assessment
print(f"\nYour Entered Password: {masked_password}")
print(f"\nPassword Strength Assessment: {strength_message}\n")

# Offer some helpful tips for creating a stronger password
tips = [
    "Here are some tips to help you create a stronger password:",
    "1. Length: Aim for a password that's at least 12 characters long.",
    "2. Variety: Use a mix of uppercase and lowercase letters, numbers, and special characters.",
    "3. Avoid Common Words: Steer clear of easily guessable words or phrases.",
    "4. No Personal Details: Don't use names, birthdays, or other personal information.",
    "5. Use Passphrases: Consider a combination of unrelated words or a full sentence.",
    "6. Unique Passwords: Use different passwords for different accounts.",
    "7. Update Regularly: Change your passwords periodically for added security.",
    "8. Two-Factor Authentication: Enable 2FA whenever possible for extra protection.",
    "9. Be Cautious: Be wary of phishing attempts and only enter your password on trusted sites.",
    "10. Consider a Password Manager: A password manager can help you keep track of unique and complex passwords."
]

# Print out the tips for creating a strong password
for tip in tips:
    print(tip)
