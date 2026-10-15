"""Cinema Ticket Price Calculator — adult + child tickets plus a flat booking fee."""

ADULT_PRICE = 19.99
CHILD_PRICE = 8.99
BOOKING_FEE = 2.50


def ticket_price(adults, children):
    return (adults * ADULT_PRICE) + (children * CHILD_PRICE) + BOOKING_FEE


if __name__ == "__main__":
    adults = int(input("Adult tickets: "))
    children = int(input("Child tickets: "))
    print(f"Total price: £{ticket_price(adults, children):.2f}")
