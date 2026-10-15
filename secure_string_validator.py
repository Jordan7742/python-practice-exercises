"""
Secure String Validator
Checks a user-entered string against several rules: length, case,
uniqueness of characters, and a sum-of-ASCII-values range. A simple
exercise in combining multiple validation conditions.
"""


def is_unique(text):
    """Return True if no character in `text` repeats."""
    return len(set(text)) == len(text)


def sum_ascii(text):
    """Return the sum of ASCII values of every character in `text`."""
    return sum(ord(char) for char in text)


def validate(text):
    checks = {
        "Length is between 5 and 7 characters": 5 <= len(text) <= 7,
        "Only uppercase letters": text.isupper(),
        "Letters only (no numbers)": text.isalpha(),
        "All characters are unique": is_unique(text),
        "ASCII sum is between 420 and 600": 420 <= sum_ascii(text) <= 600,
    }

    for rule, passed in checks.items():
        status = "OK" if passed else "FAILED"
        print(f"[{status}] {rule}")

    return all(checks.values())


if __name__ == "__main__":
    user_input = input(
        "Enter a word (5-7 chars, unique uppercase letters, "
        "ASCII sum between 420-600): "
    )
    if validate(user_input):
        print("\nValid string!")
    else:
        print("\nInvalid string — see failed checks above.")
