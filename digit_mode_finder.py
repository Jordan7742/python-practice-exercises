"""
Digit Mode Finder
Finds the most frequently occurring digit(s) in a user-entered number,
and detects whether the data is multimodal (more than one most-common value).
"""

from statistics import multimode

expected_digit_count = int(input("How many digits would you like to type? "))
digits = input("Type your digits: ")

if len(digits) != expected_digit_count:
    print("The number of digits typed does not match what you specified.")
else:
    modes = multimode(digits)
    appears = digits.count(modes[0])

    print(f"The most common digit(s): {modes}, appearing {appears} time(s).")

    if len(modes) > 1:
        print("Your data is multimodal.")
