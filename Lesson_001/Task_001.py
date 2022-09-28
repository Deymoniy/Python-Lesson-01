print('Hello, username. Please enter a number from 1 - 7 which will signify the day of the week.')
day = int(input())
if day >= 1 and day <= 5:
    print("Too bad, it's not a weekend.")
elif day > 5 and day <= 7:
    print("Wohoo, That's a weekend my boy.")
else:
    print("You've picked a wrong number.")
