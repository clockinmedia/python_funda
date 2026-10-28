# Program 1: Input Handling
# Asks the user for their name and age, validating the age.

name = input("Enter your name: ").strip()
while name == "":
    name = input("Name can't be blank. Enter your name: ").strip()

while True:
    age_text = input("Enter your age: ")
    if age_text.isdigit() and 0 < int(age_text) < 120:
        age = int(age_text)
        break
    print("Please enter a whole number between 1 and 119.")

print(f"Hi {name}! Next year you'll be {age + 1}.")
