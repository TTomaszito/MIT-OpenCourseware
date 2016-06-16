# Problem Set 1
# Name: Tomasz Turek
# Collaborators: n/a
# Time Spent: 20 min

balance = float(raw_input("What is your outstanding balance on the credit card ?"))
intrestRate = float(raw_input("What is your annual interest rate?"))
monthlyPayments = float(raw_input("What is your minimum monthly payment rate?"))

month = int(0)
totalPaid = float(0)

while (month < 12 ):

    minMonthlyPayments = round(monthlyPayments * balance , 2)
    
    intrestPaid = round((intrestRate/12)*balance , 2)
 
    principalPaid = minMonthlyPayments - intrestPaid
 
    balance = balance - principalPaid
    
    totalPaid = totalPaid + minMonthlyPayments
    
    month  = month  + 1

    print str("Month: "),month
    print str("Minimum monthly payment: $"),minMonthlyPayments
    print str("Principal Paid: $"),principalPaid
    print str("Remaining Balance: $"),balance

print str("RESULT")
print str("Total amount paid: $"),totalPaid
print str("Remaining balance: $"), balance

    
