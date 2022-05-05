# Variable for list
groceries = []

#Impliment a variable for the user to save grocery list as txt file
list=open("Grocery_list", "w")



#ask user for items to index

item = ''


while item != 'done':
    item = input('what item are you shopping for? type done when finished: ')
    if groceries!= 'done':
        groceries.append(item)





#show the shopping list to the user // use list variable to write user input
print('your shopping list is: ')
for i in groceries:
    print("\t" + i)
    list.write(i+"\n")

list.close()


        
#create a loop until item list is finished // ask user what to remove from list
while len(groceries) > 0:
    item = input('What would you like to remove from list? ')
    groceries.remove(item)


    
#when list is 0 print recipt
print('Here is your recipt: ')

f  = open('Grocery_list', 'r')
lineno = 1
for line in f:
  print (str(lineno) + ':' + line.strip())
  lineno = lineno + 1
f.close

    




