from filecmp import cmp
import time
import sys
import json
import filecmp

#cool print effect
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)



#Variables for pokemon
#Pokemon={}

"""_________________________________________Users Pokemon stats / saved to dict____________________________________________________"""

UsersPoke = open("UPoke.json", "w")

print ("Please enther the required information for each Pokemon up to 3. Type 'q' when done.")
def UPoke1(poke_name, hp, defense, type):
    poke_name = poke_name.strip()
    hp = hp.strip()
    defense = defense.strip()
    type = type.strip()

    Pokemon = {"Name":poke_name, "HP":hp, "DEF:":defense, "Type": type}
    return Pokemon

#user Input for their Pokemon
    
while True:
    
    poke_name = input ("Enter The Pokemon Name: ")
    hp = input ("Enter your Pokemons HP: ")
    defense = input ("Enter your pokemons Defense: ")
    type = input ("What is your Pokemons Type ('water,fire,grass): ")

    if poke_name != 'q' or hp != 'q' or defense != "q" or type != "q" :
        Pokemon = UPoke1(poke_name, hp, defense, type)
        UsersPoke.write(str(Pokemon))
    else:
        delay_print ("Saving...\n")
        break
    
UsersPoke.close()
    
"""_______________________________________Enemy Pokemon______________________________________"""

#Ask user what they are battling

EPoke = open("EPoke.json", "w")

print ("Please enther the required information for the Pokemon you are fighting. Type 'q' when done.")
def EPoke1(poke_name, hp, defense, type):
    poke_name = poke_name.strip()
    hp = hp.strip()
    defense = defense.strip()
    type = type.strip()

    EPokemon = {"Name":poke_name, "HP":hp, "DEF:":defense, "Type": type}
    return EPokemon

#user Input for the enemy Pokemon
    
while True:
    
    poke_name = input ("Enter The Pokemon Name: ")
    hp = input ("Enter Enemy Pokemons HP: ")
    defense = input ("Enter Enemy pokemons Defense: ")
    type = input ("What is Enemy Pokemons Type ('water,fire,grass): ")

    if poke_name != 'q':# or hp != 'q' or defense != "q" or type != "q" :
        EPokemon = EPoke1(poke_name, hp, defense, type)
        EPoke.write(str(EPokemon))
    else:
        delay_print ("Saving...\n")
        break
    
EPoke.close()

"""_________________Compare Enemy Pokemon to Users and Tell user which pokemon is best_________________"""
EPokeType = {EPoke1[3]}

print (EPokeType)







# ALL """ COMMENTED CODE HEREAFTER WERE UNSUCSESSFUL ATTEMPTS TO CALL DATE STORED IN U/EPoke to use as variables for comparision.


# Compare enemy pokemon to users by type

"""
Type = ["Fire", "water", "grass"]
f = open ('UPoke', 'r')
print(f.read())
"""


"""
f1 = UsersPoke
f2 = EPoke
result=filecmp.cmp(f1, f2)
print(result)
"""


"""
EPoke.keys()
['Type']
for key in EPoke.keys(): print(key)
"""

with open('UPoke.json') as json_file:
    data = json.load(json_file)
    print(data)



#Take inputed data from UPoke and EPoke and turn into variable.



#Take U/EPoke variables HP, DEF, Type and compare 



#Tell user What UPoke is best to defeat EPoke.



