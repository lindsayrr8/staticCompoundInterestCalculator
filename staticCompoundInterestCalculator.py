
# This program calculates an account balance of $1,000
# at 5% interest after 3 years.

# Declarations: constant account balance;
# Calculates compounding interest plus initial account balance;
# Rounds results to two decimal places for currency, stored as variables;
# Outputs results to user.

INITIALBALANCE = 1000
yearOne = (INITIALBALANCE)*0.05 + INITIALBALANCE
yearTwo = (yearOne)*0.05 + (yearOne)
yearThree = (yearTwo)*0.05 + (yearTwo)
roundYearOne = round(yearOne, 2)
roundYearTwo = round(yearTwo, 2)
roundYearThree = round(yearThree, 2)

print("Initial account balance = $1,000." )
print (' ')
print("Calculating annual increase at 5% interest..." )

print (' ')

print("Year one:", "$", roundYearOne)
print("Year two:", "$", roundYearTwo)
print("Year three:", "$", roundYearThree)
