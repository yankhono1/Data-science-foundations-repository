print("Welcome")

age = int(input("Enter your age: "))
# This code will first check for the age group 100 and above, then move to 65 and above. 
# Individuals aged 65 or older receive the response "Enjoy your retirement!" without being categorized under "You're over the hill.
if age >= 100:
    response = "Sorry you're deaad"
elif age >= 65:
    response = "Enjoy your retirement!"
elif age >= 40:
    response = "You're over the hill"
elif age >= 21:
    response = "Congrats on your 21st"
elif age > 13:
    response = "You qualify for the kiddie discount"
else:
    response = "Age is but a number."

# the order of the elif statements are important
print(response)
