"""
People Counter
Tracks how many people are in a venue (capped at 50, with a "form a
queue" message once full), and keeps a hidden count of how many times
someone tried to decrease below zero.
"""

total_people = 0
underflow_attempts = 0


def increase(count):
    count += 1
    if count > 50:
        print("Capacity reached — please form a queue.")
        return 50
    return count


def decrease(count):
    return count - 1


if __name__ == "__main__":
    while True:
        action = input("Increase or Decrease (or 'quit'): ").strip().lower()

        if action == "increase":
            total_people = increase(total_people)
            print(total_people)
        elif action == "decrease":
            total_people = decrease(total_people)
            if total_people < 0:
                underflow_attempts += 1
                total_people = 0
                print(total_people, underflow_attempts)
        elif action == "quit":
            break
        else:
            print("Please type 'Increase' or 'Decrease'.")
