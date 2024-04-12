# ================== Compilation or syntax errors ==================

# === Example 1 ===

print("Hello World!")
# The print keyword has a capital 'P', but  Python is case sensitive so Print and print are two different things.

# === Example 2 ===

x=5 # had to also define x
if x == 5:
     print("x is equal to 5")
# The semicolon is incorrectly used to indicate the end of a line of code.
# To fix this error, the semicolon should be removed and replaced with a colon ':' to indicate the start of the block of code to be executed if the condition is true.

# === Example 3 ===

moms_age = 45
dads_age = 43
age_difference = moms_age - dads_age
print (f"The age difference between mom and dad is {age_difference}")

# As you can see, there are a few errors in this example.
# The line 'dads_age = "43"' is unnecessarily indented.
# The variable 'dads_age' is assigned a string value instead of an integer value. This can be fixed by simply removing the quotes.
# (Alternatively, you can cast the string 'dads_age' to an integer like this 'int(dads_age)'. This is considered a runtime error (more on this below) as 'age_difference' is unable to concatenate a string and an integer type.)
# The print statement is missing parentheses and the variable 'age_difference' is missing curly braces required for f-string formatting.

# ================== Runtime errors  ==================
# === Example 1 ===

word = "Python"
character = word[5]
print(character) # needed a print statement
# As you can see, 'character' is trying to access the seventh element (6th index) in a word with only 6 letters (having indices 0 - 5). Remember: indexing starts at 0, so this statement is referencing an index that is out of bounds.

# === Example 2 ===

a = 5
b = 2 # acceptable division
c = a / b
print(c)

# Variable 'c' will encounter a 'division by zero' runtime error as dividing an integer by 0 is considered an illegal operation in Python.

# === Example 2 ===

a = 5
b = 7
c = a + b
print(c) # added a print statement
# The program is attempting to concatenate a string and an integer, which is not a valid operation. The solution here is to cast the string to an integer to avoid 'type errors'.

# ================== Logical errors ==================

# === Example 1 ===

area_trapezoid = (3 + 5) * 6 / 2
print(area_trapezoid)

# The code above should calculate the area of a Trapezoid with parallel sides of length 3 and 5, and a height of 6.
# The area of this trapezoid should be 24, but when you run this program, you see that this is not the case. The error arises due to the incorrect order of operations. 
# The solution here is to add the missing brackets around 3 + 5
# The statement should be:
#       area_trapezoid = (3 + 5) * 6 / 2

# === Example 2 ===

numbers = [1, 2, 3, 4, 5]
sum = 0

for i in range(len(numbers)):
    sum += numbers[i]

print("The sum of the numbers is: ", sum)

# This code intends to calculate the sum of the numbers in the numbers list. 
# The problem, however, is that the logic in the loop condition is incorrect as it will attempt to access the numbers list using indices 5-9, which do not exist.
# The solution is to change the loop condition to loop over the indices of the numbers list, rather than a fixed range:
#       for i in range(len(numbers)):
#           sum += numbers[i]

# === Example 3 ===

# The logical error in the above code is the order of the if statements. 
# Since the if statements are evaluated in order, the current code will first check if 'grade_score' is greater than 50, which is True since 'grade_score' is 80, so it will print "Grade: C" and skip the remaining statements. 
# The subsequent elif statements will not be evaluated, so "Grade: C" will always be printed.

# To fix this issue, the order of the if and elif statements should be reversed, so that the most restrictive conditions are checked first, like this:
grade_score = 80
if grade_score > 85:
       print("Grade: A")
elif grade_score > 75:
       print("Grade: B")
elif grade_score > 50:
       print("Grade: C")
else:
       print("Grade: F")
