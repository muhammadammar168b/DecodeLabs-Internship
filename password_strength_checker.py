"""
Cyber Security - Project 1
Password Strength Checker
DecodeLabs Industrial Training Kit - Batch 2026
"""

import re

# A small sample list of commonly leaked/weak passwords (bonus feature)
COMMON_PASSWORDS = {
    "123456", "password", "123456789", "qwerty", "abc123",
    "111111", "123123", "letmein", "iloveyou", "admin"
}


def check_password_strength(password: str) -> dict:
    """
    Analyzes a password and returns a dictionary containing
    the individual checks and the overall strength rating.
    """
    length = len(password)
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'[0-9]', password))
    has_symbol = bool(re.search(r'[!@#$%^&*(),.?":{}|<>_\-+=~`\[\];\'\\/]', password))
    is_common = password.lower() in COMMON_PASSWORDS

    score = 0

    # Length checks
    if length >= 8:
        score += 1
    if length >= 12:
        score += 1

    # Character variety checks
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_symbol:
        score += 1

    # Penalty for common/leaked passwords
    if is_common:
        score = 0

    # Determine strength label
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return {
        "password": password,
        "length": length,
        "has_upper": has_upper,
        "has_lower": has_lower,
        "has_digit": has_digit,
        "has_symbol": has_symbol,
        "is_common": is_common,
        "score": score,
        "strength": strength,
    }


def print_report(result: dict) -> None:
    """Nicely prints the password analysis report."""
    print("\n----- Password Strength Report -----")
    print(f"Password        : {'*' * result['length']}")
    print(f"Length          : {result['length']} characters")
    print(f"Uppercase used  : {'Yes' if result['has_upper'] else 'No'}")
    print(f"Lowercase used  : {'Yes' if result['has_lower'] else 'No'}")
    print(f"Digit used      : {'Yes' if result['has_digit'] else 'No'}")
    print(f"Symbol used     : {'Yes' if result['has_symbol'] else 'No'}")
    print(f"Common/Leaked   : {'Yes (High Risk!)' if result['is_common'] else 'No'}")
    print(f"Score           : {result['score']} / 6")
    print(f"STRENGTH RESULT : {result['strength']}")
    print("-------------------------------------\n")


def main():
    print("=====================================")
    print("   Password Strength Checker")
    print("=====================================")

    while True:
        password = input("Enter a password to check (or 'q' to quit): ")
        if password.lower() == 'q':
            print("Goodbye! Stay secure.")
            break

        result = check_password_strength(password)
        print_report(result)


if __name__ == "__main__":
    main()