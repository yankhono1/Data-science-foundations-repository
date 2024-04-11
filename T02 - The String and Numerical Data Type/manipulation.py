print("Welcome")

user_input = input("Please enter a sentence: ")

str_manip = (user_input)

# Calculate and display the length of str_manip
print(len(str_manip))

# Find the last letter in str_manip. Replace every occurance of this letter with @
# Creat a variable to store the sentence and modify it.

last_letter = str_manip[-1]
manipulated_sentence = str_manip.replace(last_letter, "@")

print(manipulated_sentence)

# Print the last three letters in str_manip backwards added [::-1] for the reverse order

three_letters_back = str_manip[-3:][:: -1]

print(three_letters_back)


# 5 letter word of made up of first 3 and last 2 characters

new_word = manipulated_sentence[:3] + manipulated_sentence[-2:]

print(new_word)
