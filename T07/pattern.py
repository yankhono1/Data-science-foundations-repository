# add pattern as string 
pattern = "*"
# create for loop iterating in the range from 1 - 10
for row in range(1, 10):
    if row <= 5:
        # print pattern multiplied by row
        print(pattern * row)
        
    # else if row is greater than 5 
    else:
        # print pattern multiplied by 10 minus current row (will print in descending order 5,4,3,2,1)
        print(pattern * (10 - row)) # does brackets first
        # so the pattern will multiply the row when descending because of the minus 
