# Credit Card debt - paying debt off in a year(bisection search)
# variables provided by edX test engine: 
#    balance - outstanding balance of credit card
#    annualInterestRate - annual interest rate
# 
# Example: 
#   balance = 320000
#   annualInterestRate = 0.2
# ----- Output -----
# Lowest Payment: 29157.09
#

min_fixed_payment = 0
remaining_balance = 0 

monthly_interest_rate = annualInterestRate/12.0
lower_bound = balance/12.0
upper_bound = (balance * (1 + monthly_interest_rate)**12) / 12.0

while True:
    min_fixed_payment = (lower_bound + upper_bound) / 2.0
    temp_balance = balance

    for month in range(1,13):        
        remaining_balance = temp_balance - min_fixed_payment
        temp_balance = remaining_balance + (monthly_interest_rate * remaining_balance)
    if round(remaining_balance, 2) == 0.0:
        print "Lowest Payment: " + str(round(min_fixed_payment, 2))
        break
    if temp_balance > 0:
        lower_bound = min_fixed_payment
    elif temp_balance < 0:        
        upper_bound = min_fixed_payment

