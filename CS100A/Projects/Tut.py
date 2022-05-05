import random

name = input("what is your name: " ) #Ask user their name.

correct = 0

x = random.randint(1,10)
y = random.randint(1, 10)

ans = input('what is', + str(x) + '*' + str (y) + '? ')
ans = int (ans)
if ans == x*y:
    print('you got it')
    correct = correct + 1
else:
    print('Dang. ', x, '*', y, '=' (x+y))

    x = random.randint(1,10)
y = random.randint(1, 10)

ans = input('what is', + str(x) + '+' + str (y) + '? ')
ans = int (ans)
if ans == x+y:
    print('you got it')
    correct = correct + 1
else:
    print('Dang. ', x, '+', y, 'y' (x+y))

print ('you got')