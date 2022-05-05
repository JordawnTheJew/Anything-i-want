"""
first = ['this', "is", 'list']
evens = [2,4,6,8,10]
students = ['abigail', 'ben','christi','dave']

print(first)
print(evens + students)

for e in evens:
    print(str(e) + ' is 2 * ' + str(int(e/2)))


miditem = len(students)//2
print(students[-2])
"""


team = []


player = ''
while player != 'done':
    player = input('give me a player name then type done when finished: ')
    if player != 'done':
        team.append(player)

if player == 'done' and len(team)== 0:
    print ('you didnt enter any members')



print('your team is: ')

for p in team:
    print("\t" + p)

if 'pete' in team:
    print("Icant wait to play")
else 'pete' not in team:
    print("put me in coach im ready to play")

