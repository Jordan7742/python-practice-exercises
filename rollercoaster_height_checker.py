"""
Rollercoaster Height Checker
Checks riders against a theme-park-style height/companion rule, and
stops once 8 "ride units" worth of people have been allowed through
(an adult riding alone counts for 2 units, a child with an adult for 1).
"""

allowed_units = 0

while allowed_units < 8:
    height = int(input("Input height in cm: "))
    with_adult = input("Are you riding with an adult? (Y/N): ").upper()

    if height > 119 and with_adult == "Y":
        print("You can ride!")
        allowed_units += 2
    elif height > 139 and with_adult == "N":
        print("You can ride!")
        allowed_units += 1
    elif height > 139 and with_adult == "Y":
        print("You can ride!")
        allowed_units += 2
    else:
        print("Sorry, you can't ride.")
