# Problem Set 1
# Name: Tomasz Turek
# Collaborators: n/a
# Time Spent: 120 min

balance = float(raw_input("What is your outstanding balance on the credit card ? "))
intrestRate = float(raw_input("What is your annual interest rate? "))
oryginalBalance = balance
 

month = int(0)
minMonthlyPayment = int(10)
monthlyIntrestRate = intrestRate/int(12.0)


   
while (month <= 12 and balance > 0):
        
    balance = round(balance*(1+monthlyIntrestRate)-minMonthlyPayment,2)
    
    month += 1
    
    if ( month == 12 and balance > 0):
        
        month = 0
        
        minMonthlyPayment = minMonthlyPayment+10
        
        balance = oryginalBalance
        
    
    
print "Number of months needed: ", month
print "Monthly payment to pay off debt in 1 year: ", minMonthlyPayment
print "Balance: ", balance  
