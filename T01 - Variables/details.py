# Here is a vaiable for taking user's name
name = input("Please enter your name: ")

# Variable for user's age
age = input("Please enter your age: ")

# Variable for user's house number
house_number = input("Please enter your house number: ")

# Variable for user's street name
street_name = input("Please enter your street name: ")

# I will use the fstring funtion to call the variables and construct the sentence
sentence = f"This is {name}. He is {age} years old and lives at house number {house_number} on {street_name} street."

# Here I am printing the sentence
print(sentence)
