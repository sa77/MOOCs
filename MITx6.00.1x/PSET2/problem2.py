# Credit Card debt - paying debt off in a year(multiples of 10)
# variables provided by edX test engine: 
#    balance - outstanding balance of credit card
#    annualInterestRate - annual interest rate
# 
# Example: 
# 	balance = 3229
#  	annualInterestRate = 0.2
# ----- Output -----
# Lowest Payment: 310
#

min_fixed_payment = 0
remaining_balance = 0 
total_paid = 0

while True:
    temp_balance = balance
    min_fixed_payment += 10
    for month in range(1,13):        
        remaining_balance = temp_balance - min_fixed_payment
        temp_balance = remaining_balance + ((annualInterestRate/12.0) * remaining_balance)
    if remaining_balance <= 0:
        print "Lowest Payment: " + str(min_fixed_payment)
        break

