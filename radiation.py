# Define the lists to store locations and their radiation levels
locations = ["Urban", "Forest"]
levels = [[18, 20, 22], [12, 14, 15]]

# Process each location's data and calculate the average radiation level
# iterate through a list
for i, location in enumerate(locations):
    # Print the location and levels being processed
    print(f"\nDebug: Processing location {location} with levels {levels[i]}")
    average = sum(levels[i]) / len(levels[i])
    print(f"{location} Average Radiation Level: {average}")

# Now we'll write the part that allows continuous data input using a while loop
measurements = []
# Inform the user that the data entry process is starting
print("\nBegin entering new radiation levels. Type 'done' to finish.\n")

# This loop will run indefinitely until 'done' is entered
while True:
    level = input("\nEnter radiation level or 'done' to finish: ")
    if level.lower() == 'done':
        # Confirm that the loop exit condition has been met
        print("Debug: Exiting input loop.")
        break
    try:
        # Convert the input to an integer and add to the measurements list
        new_level = int(level)
        measurements.append(new_level)
        # Confirm that a new level has been added
        print(f"Debug: Added level {new_level}")
    except ValueError:
        # Inform the user of an invalid input
        print("Invalid input. Please enter a valid number or 'done'.")

# Calculate and display the average of the new measurements
if measurements:
    average = sum(measurements) / len(measurements)
    print(f"New Measurements Average Radiation Level: {average}")
else:
    # Inform the user that no new measurements were entered
    print("Debug: No new measurements were entered.")
