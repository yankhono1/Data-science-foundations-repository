print("Welcome \nCongragulations on completing the triathalon!") 

# a program that detenmines the award a person competing in a triatholon will recieve
# read in the times in minutes for all three events of a triathalon (swimming, cycling, and running) 
swimming = int(input("Please enter your swimming time in minutes: "))
cycling = int(input("Please enter your cycling time in minutes: "))
running = int(input("Please enter your running time in minutes: "))
# calculate and display the total time taken to to complete the triathanlon 
total_time = swimming + cycling + running

# more than 10 minutes off from the qualifiying time
if total_time >= 111:
    response = "No award"
# within 10 minutes of the qualifying time. 106 to 110 minutes. Provincial 
elif total_time >= 106 and total_time < 110:
    response = "Provincial"
# within 5 minutes of the qualifying time. 101 to 105 minutes. Provincial Half Colours
elif total_time >= 101 and total_time < 105:
    response = "Provincial Half Colours"
# within the qualifying time. 0 to 100 minutes. Provincial colours
elif total_time <= 100:
    response = "Provincial Colours"

else: 
    response = "You do not qualify for an award"

print(response)
# the total time needed for the award is 100 minutes
# *if float change into an integer (round up)*
