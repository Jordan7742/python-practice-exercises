"""
Typing Speed Calculator
Estimates the number of key presses needed to type a phrase on an old
multi-tap phone keypad, where each letter needs a different number of
presses depending on its position on its key (like T9 texting).
"""

PRESSES_PER_LETTER = {
    1: "ADGJMPTW",
    2: "BEHKNQUX",
    3: "CFILORVY",
    4: "SZ",
}


def presses(phrase):
    """Return the total number of key presses needed to type `phrase`
    (expects uppercase letters only)."""
    count = 0
    for char in phrase:
        for press_count, letters in PRESSES_PER_LETTER.items():
            if char in letters:
                count += press_count
                break
    return count


if __name__ == "__main__":
    message = input("Type a phrase (UPPER case letters only): ")
    print(presses(message))
