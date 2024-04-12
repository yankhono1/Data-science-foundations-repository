import math 

# calculates interest you'll earn on your investment or calculate your bond payment on the house
# capitalisation should not impact anything- could use lower() function to fix this issue
investment = "Investment - calculate the amount of interest you will earn on your investment"
bond = "Bond - calculate the amount you will have to pay on a home loan"

print("Investment - calculate the amount of interest you will earn on your investment")
print("Bond - to calculate the amount you will have to pay on a home loan")

user_input = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

user_input = user_input.lower()

# INVESTMENT
# the amount of money they are depositing (p)
investment_deposit = int(input("What is the amount that the user deposit: "))

# amount of interest once applied (A)
amount_interest_applied = int(input("what is the amount of interest applied ")) 
# inerest rate (r)
investment_interest = amount_interest_applied / 100

# the number of years they are planning on investing (t)
num_years = int(input("What is the number of years that the money has been invested: "))


investment_simple_interest = investment_deposit* 1 + investment_interest * num_years

investment_compound_interest = investment_deposit * math.pow((1+investment_interest), num_years)

# BOND

# present value of the house
present_value = int(input("Please input the present value of the house"))

#interest rate (dividing by 12 when calculating per month)
bond_interest = int(input("Please enter the interest rate of the house per year: " )) /100 / 12

# number of months for repayment
num_months = int(input("Please enter the number of months you plan to to take repay the bond: "))

bond_repayment = (bond_interest *present_value)/ (1 - (1 + bond_interest) ** (-num_months))
repay_bond_sentence = f"You will have to repay {bond_repayment} per month"

if user_input == bond:
    print(repay_bond_sentence)
elif user_input == investment:
    print(investment_deposit, amount_interest_applied, num_years)
    print()
else:
    print("Please enter 'investment' or 'bond'... ")

# investment formula 
