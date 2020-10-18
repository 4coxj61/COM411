print("\nWhat is your name human?")
name = input()

print("\nHow old are you (in years)?")
age = int(input())

print("\nHow tall are you (in metres)?")
height = float(input())

print("\nHow much do you weigh (in kilograms)?")
weight = float(input())

bmi = weight/(height**2)

print(name, "your bmi is", bmi)