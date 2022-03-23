import time
import sys

#cool print effect
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)



#Variables for pokemon
#Pokemon={}


UsersPoke = open("UPoke", "w")

print ("Please enther the required information for each Pokemon up to 3. Type 'q' when done.")
def UPoke1(poke_name, hp, defense, type):
    poke_name = poke_name.srtip()
    hp = hp.strip()
    defense = defense.strip()
    type = type.strip()

    Pokemon = {"Name":poke_name, "HP":hp, "DEF:":defense, "Type": type}
    #return Pokemon

#user Input for their Pokemon
    
while True:
    
    poke_name = input ("Enter The Pokemon Name: ")
    hp = input ("Enter your Pokemons HP: ")
    defense = input ("Enter your pokemons Defense: ")
    type = input ("What is your Pokemons Type ('water,fire,grass): ")

    if poke_name != 'q' or hp != 'q' or defense != "q" or type != "q" :
        delay_print ("Saving...\n")
        break
    UsersPoke.write( str(Pokemon))
    
    UsersPoke.close()
    





#Ask user what they are battling




