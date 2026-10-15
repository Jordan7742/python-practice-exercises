"""Quarter of the Year — prints which quarter a given month number falls in."""

month = int(input("Enter the number of the month: "))

if 1 <= month <= 3:
    print("That's in the first quarter of the year.")
elif 4 <= month <= 6:
    print("That's in the second quarter of the year.")
elif 7 <= month <= 9:
    print("That's in the third quarter of the year.")
elif 10 <= month <= 12:
    print("That's in the final quarter of the year.")
else:
    print("That's not a valid month number.")
