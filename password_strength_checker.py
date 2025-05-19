import re

# Optional: Add more if needed
common_passwords = ['123456', 'password', '123456789', 'qwerty', 'abc123', '111111', '123123']

def check_password_strength(password):
    strength = 0
    feedback = []

    # Length check
    if len(password) >= 12:
        strength += 2
    elif len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password is too short (use at least 12 characters).")

    # Character variety
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Add lowercase letters.")

    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Add uppercase letters.")

    if re.search(r'\d', password):
        strength += 1
    else:
        feedback.append("Add numbers.")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        feedback.append("Add special characters.")

    # Check against common passwords
    if password.lower() in common_passwords:
        strength = 0
        feedback = ["This password is extremely common. Choose something more unique."]

    # Final evaluation
    if strength >= 6:
        rating = "Strong"
    elif strength >= 4:
        rating = "Moderate"
    else:
        rating = "Weak"

    return rating, feedback

def main():
    print("🔐 Password Strength Checker")
    password = input("Enter your password: ")
    rating, feedback = check_password_strength(password)

    print(f"\nPassword Rating: {rating}")
    if feedback:
        print("Suggestions:")
        for f in feedback:
            print(f"- {f}")

if __name__ == "__main__":
    main()
