print('Please enter the following information about your loan.')

principle = input('Principle:')
interestRate = input('interest rate percentage:')
loanTermInYears = input('loan term in years:')
newBalance = 0

#convert strings into floats for calculation.

principle = float(principle)
interestRate = float(interestRate)
loanTermInYears = float(loanTermInYears)
newBalance = float(newBalance)

#convertions

principle = principle * 1.06
numberOfPayments = loanTermInYears*12
interestRate = interestRate / 1200

#calculations (Monthly payment, interest, new balance)

monthlyPayment = (principle * interestRate * (1 + interestRate) ** numberOfPayments) / ((1 + interestRate) ** numberOfPayments - 1)
interest = (interestRate * principle)
totalEndCost = monthlyPayment * numberOfPayments

print('')
print('Monthly payment: $' + str(round(monthlyPayment,2)))
print('')
print('Total loan cost: $' + str(round(totalEndCost,2)))
print('') 