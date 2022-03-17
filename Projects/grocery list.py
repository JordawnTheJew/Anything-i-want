# Variable for list
item=0
price=0
quantity=0
groceries = []



#ask user for items to index
item = ''
while item != 'done':
    item = input('what item are you shopping for? type done when finished: ')
    if groceries!= 'done':
        groceries.append(item)

#show the shopping list to the user
print('your shopping list is: ')
for i in groceries:
    print("\t" + i)
        
#create a loop until item list is finished/ ask user what to remove from list
while len(groceries) > 0:
    item = input('What would you like to remove from list? ')
    groceries.remove(item)
 
#when list is 0 print recipt





