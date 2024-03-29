import math

# calculates interest you'll earn on your investment or calculate your bond payment on the house
# capitalisation should not impact anything- could use lower() function to fix this issue

print("Welcome \n")

# Ask user to input either "investment" or "bond" 
user_input = input("Enter either 'investment' or 'bond': ").lower()

# INVESTMENT
if user_input == "investment":
    investment_deposit = float(input("Deposit amount: "))
    interest_rate = float(input("Interest rate (%): ")) / 100
    years = int(input("Number of years: "))
    
    print("Simple or compound interest?")
    interest_type = input("Enter 'simple' or 'compound': ").lower()
    
    if interest_type == "simple":
        interest = investment_deposit * interest_rate * years 
        print(f"Simple interest: {interest}")
    
    elif interest_type == "compound":
        interest = investment_deposit * (1 + interest_rate) ** years
        print(f"Compound interest: {interest}")
        
    else:
        print("Invalid interest type")
        
# BOND        
elif user_input == "bond":
    present_value = float(input("Present value of house: "))  
    interest_rate = float(input("Interest rate (% per year): ")) / 100 / 12
    months = int(input("Number of months: "))
    
    repayment = (interest_rate * present_value) / (1 - (1 + interest_rate) ** (-months))
    print(f"Monthly repayment: {repayment}")
    
else:
    print("Invalid input")
