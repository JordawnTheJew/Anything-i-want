f=open('madlib.txt', 'r')

story=''
for line in f:
    if line.startswith("*"):
        text=input("Give me a(n) "+ line[1:].strip()+': ')
    else:
        text=line
    story = story + " " + text.strip()

print("here is your story\n")

print(story)

f.close

f.open('madlib.txt', "w")
f.write(story)
f.close()
