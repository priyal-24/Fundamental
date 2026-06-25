print("Welcome to the Interactive Personal Data Collector")

name = input("\nPlease enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in meters: "))
favourite_number = int(input("Please enter your favourite number: "))

print("\nThank you! Here is the information we collected:\n")

print(f"Name: {name} (Type: {type(name)}, Memory Address: {id(name)})")
print(f"Age: {age} (Type: {type(age)}, Memory Address: {id(age)})")
print(f"Height: {height} (Type: {type(height)}, Memory Address: {id(height)})")
print(f"Favourite Number: {favourite_number} (Type: {type(favourite_number)}, Memory Address: {id(favourite_number)})")

birth_year = 2026 - age

print(f"\nYour birth year is approximately: {birth_year} (based on your age of {age})")

print("\nThank you for using the personal data collector. Goodbye!")