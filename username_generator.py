"""Username Generator — builds a username from first initial + surname + birth year."""

first_name = input("First name: ")
surname = input("Surname: ")
year = input("Year of birth: ")

username = first_name[0] + surname + year
print(username)
