# Credit Card debt - paying the minimum
# variables provided by edX test engine: 
#    balance - outstanding balance of credit card
#    annualInterestRate - annual interest rate
#    monthlyPaymentRate - monthly minimum payment rate
# 
# Example: 
#  balance = 4213
#  annualInterestRate = 0.2
#  monthlyPaymentRate = 0.04
# ----- Output -----
# Total paid: 1775.55
# Remaining balance: 3147.67
#

min_monthly_payment = 0
remaining_balance = 0 
total_paid = 0

for month in range(1,13):
    min_monthly_payment = balance * monthlyPaymentRate
    remaining_balance = balance - min_monthly_payment
    balance = remaining_balance + ((annualInterestRate/12.0) * remaining_balance)
    total_paid += min_monthly_payment
    print "Month: " + str(month)
    print "Minimum monthly payment: " + str(round(min_monthly_payment, 2))
    print "Remaining balance: " + str(round(balance, 2))

print "Total paid: " + str(round(total_paid, 2))
print "Remaining balance: " + str(round(balance, 2))

