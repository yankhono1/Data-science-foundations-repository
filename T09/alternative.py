print("Welcome\n")

# capitalise every other CHARACTER
# Ask the user to input a sentence and store it in a variable called user_input
user_input = input("Enter a sentence, we will capitalise every other cHaRaChTeR: ")

# an empty string to store the modified sentence
new_string = ""

# Loop through each character in the input sentence along with its index
# The enumerate() function in the for loop goes through each character in the user_input string 
# it also provides both the index (i) and the character (char) for each iteration.
for i, char in enumerate(user_input):
    # Check if the index i is even (divisible by 2 with remainder 0)
    if i % 2 == 0:
        # If the index is even, add the uppercase version of the character to new_string
        new_string += char.upper()
    else:
        # If the index is odd, add the lowercase version of the character to new_string
        new_string += char.lower()

# Print the modified sentence with alternate letters capitalized
print(new_string)

# capitalise every other WORD
word_capital = input("\nEnter a new sentence, we will capitalise EVERY other WORD: ")
words = word_capital.split()  # Split the sentence into a list of words
new_sentence2 = ""

for i, word in enumerate(words):
    if i % 2 == 0:
        new_sentence2 += word.upper()  # Capitalize alternate words
    else:
        new_sentence2 += word.lower()  # Keep other words as lowercase
    new_sentence2 += " "  # Add a space between words

print(new_sentence2[:-1])  # Print the modified sentence, excluding the extra space at the end

