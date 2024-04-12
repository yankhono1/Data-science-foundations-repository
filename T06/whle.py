# Create empty list 
numbers = []

# Loop to continuously prompt for input
while True:

  # Get user input
  user_input = int(input('Enter a number: '))    

    # Check if the user input is -1, and stop input if true
  if user_input == -1:
    print('Stopping number input [cannot enter >0]')
    break

  # Handle valid input
  elif user_input >= 0:
    numbers.append(user_input)
    
    # Calculate and display the mean of the entered numbers
    mean = sum(numbers) / len(numbers)
    print (f'Mean so far: {mean}')

  # Handle invalid input    
  else:
    print('Invalid input. Enter a number >= 0')

  # Prompt to end outer loop
  end_program = input('Enter another number [press Q to end program]: ')  

  # Break out of outer loop
  if end_program.upper() == 'Q':
    break

print('Program ended')
