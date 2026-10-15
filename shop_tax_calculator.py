"""
Shop Tax Calculator
Calculates a total shopping bill, applying a 20% tax to flagged
luxury/"sin tax" items, and logs the result to a transactions file.
"""

TAX_RATE = 1.20

shopping = [
    ["bread", 1.20, False],
    ["tea bags", 5, False],
    ["cake", 5, True],
    ["milk", 2.0, False],
    ["cigarettes", 10, True],
]


def apply_tax(price):
    return price * TAX_RATE


def calculate_total(items):
    total = 0
    for name, price, taxable in items:
        total += apply_tax(price) if taxable else price
    return total


if __name__ == "__main__":
    total_cost = calculate_total(shopping)
    print(f"Total cost: £{total_cost:.2f}")

    with open("transactions_list.txt", "a") as file:
        file.write(f"{total_cost:.2f}\n")
