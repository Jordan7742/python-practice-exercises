"""
Teddy Bear Pay Calculator
Compares two pay structures (piece-rate vs. hourly) and reports
whichever earns more.
"""

teddies_made = int(input("How many teddies have you made? "))
hours_worked = int(input("How many hours have you worked? "))

piece_rate_pay = teddies_made * 2
hourly_pay = hours_worked * 5

if piece_rate_pay > hourly_pay:
    print(f"You have earned £{piece_rate_pay} (piece-rate pay).")
elif piece_rate_pay == hourly_pay:
    print(f"Both pay structures earn you £{piece_rate_pay}.")
else:
    print(f"You have earned £{hourly_pay} (hourly pay).")
