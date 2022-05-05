"""f = open('Reminder.txt', "w")
f.write('Practice\n')
f.write('Your\n')
f.write('Python\n')
f.close
"""

print('this is your recipt: ')

f  = open('Grocery_list', 'r')
lineno = 1
for line in f:
  print (str(lineno) + ':' + line.strip())
  lineno = lineno + 1
f.close
