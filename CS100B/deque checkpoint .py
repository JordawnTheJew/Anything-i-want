import collections
import random

class Shoppers:
    def __init__(self, person):
        self.person = person


shoppers = collections.deque()
persons = ["Gabby","Micaiah","Payge", "Isaac", "Dani"]
for name in range (1, 101):
    #fewer than 3 
    if len(shoppers) < 3:
        p = persons[random.randrange(0, len(persons))]
        print ("adding " + p + " to the line")
        shoppers.append(Shoppers(p))
    #less than 6
    if len(shoppers) > 6:
        m = shoppers.pop()
        print(m.person + " left the line p.o'ed")
    #rand number
    i = random.randrange(0,3)
    # if 0 its your turn
    if i == 0:
        m = shoppers.popleft()
        print("its your turn to check out " + m.person)
    # other add someone else to the line
    else:
        p = persons [random.randrange(0, len(persons))]
        print("adding " + p + " to the line")
        shoppers.append(Shoppers(p))



