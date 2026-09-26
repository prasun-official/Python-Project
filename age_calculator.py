from datetime import date

# Birth date input
day = int(input("Enter your birth day: "))
month = int(input("Enter your birth month: "))
year = int(input("Enter your birth year: "))

# Today's date
today = date.today()

# Calculate age
age = today.year - year

# Check if birthday has occurred this year
if (today.month, today.day) < (month, day):
    age -= 1

print("Your age is:", age, "years")