bill = float(input('What was your bill? '))

print ('your 10% tip would be $' +str(bill*.1))
tip10 = bill*.1
print ('your total with a 10% tip would be $' + str(bill +tip10))

print ('your 15% tip would be $' +str(bill*.15))
tip15 = bill*.15
print ('your total with a 15% tip would be $' + str(bill +tip15))

print ('your 20% tip would be $' +str(bill*.2))
tip20 = bill*.2
print ('your total with a 20% tip would be $' + str(bill +tip20))

print ('your 25% tip would be $' +str(bill*.25))
tip25 = bill*.25
print ('your total with a 25% tip would be $' + str(bill +tip25))

tip = int(input('What percentage would you like to tip? '))

print("Your total Bill is ", tip  /100 * bill + bill)
