"""
def welcome ():
    print('hello, welcome to this program')

    def add(x, y):
        return x+y

def sum(n):
    s = 0
    for i in range(1, n+1):
      s = s + i
    return s  


welcome()

s = sum(10)
print('sum from 1 to 10 is', s)

""""
def countalpha(text):
    alpha = 0
    for c in text:
        if c.isalpha():
            alpha = alpha+1
    return alpha

def countnumeric(text):
    number = 0
    for c in text:
        if c.isnumeric():
            number = number+1
    return number

text = input('please enter a phrase: ')

print('We looked through ' + text + ' and found:')
acount = countalpha(text)
print(str(acount) + ' alphabet characters')
ncount = countnumeric(text)
print(str(ncount) + ' numeric characters')
"""
"""
task = []
completed = []
def add(i):
    task.append(i)

#itvoyagers.in

def delete(i):
    print("n"+i + " is deleted from the list")
    task.remove(i)

#itvoyagers.in

def view():
    n = 1
    print("nTasks in list")
    for t in task:
        print(str(n)+" : "+t)
        n = n + 1
    n = 1 
    if(completed != []):
        print("Tasks Completed")
        for t in completed:
            print(str(n)+" : "+t)
            n = n + 1
    else:
        print("No task completed yetn")

#itvoyagers.in

def done(i):
    print("n"+ i + " is donen")
    task.remove(i)
    completed.append(i)