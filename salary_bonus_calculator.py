"""Salary Bonus Calculator — multiplies salary by 10 if a bonus is awarded."""

salary = int(input("Input your salary: "))
bonus = input("Have you earned a bonus? (True/False): ")

if bonus == "True":
    salary *= 10
    print(f"Your new salary is £{salary}, congrats on the bonus.")
elif bonus == "False":
    print(f"You have received no bonus, your salary is £{salary}.")
else:
    print("Please enter True or False.")
