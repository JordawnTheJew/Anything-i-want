import time
import numpy as np
import sys

# Print a character at a time

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

# Creatign a Class
class Pokemon:
    def __init__(self, name, types, moves, EVs, health='==================='):
        # Save var as attributes
        self.name = name
        self.types = types
        self.moves = moves
        self.attack = EVs ['ATTACK']
        self.defense = EVs ['DEFENSE']
        self.health = health
        self.bars = 20 # health bars shown at the end of __init__


    def fight(self, Red):  #Fight settings for two pokemon Your(self) and Red

        # Pritn fight information for you being the value of the variables in our class function.
        print("-----Red has challenged you to a pokemon battle-----")
        print(f"\n{self.name}")
        print("Your Pokemon Type: ", self.types)
        print("ATT", self.attack)
        print("DEF", self.defense)
        print("LVL:", 3*(1+np.mean([self.attack,self.defense])))
        print("\nVS")

        #Fight Information for the CPU
        ##print("-----Red has challenged you to a pokemon battle-----")
        print(f"\n{Red.name}")
        print("Reds Pokemon Type: ", Red.types)
        print("ATT", Red.attack)
        print("DEF", Red.defense)
        print("LVL:", 3*(1+np.mean([Red.attack,Red.defense])))
        
        
        time.sleep(2)

        #Type advantages
        PokeType = ['Fire', "Water", "Grass"]
        for i, k in enumerate(PokeType):
            if self.types == k:
                #neutral pokemon/ are same type
                if Red.types == k:
                    string_1_attack = '\n Its not very effective...'
                    string_2_attack = "\n Its not very effective..."

                #Reds Pokemon is strong
                if Red.types == PokeType[(i+1)%3]:
                    Red.attack *= 2
                    Red.defense *= 2
                    self.attack /= 2
                    self.defense /= 2
                    string_1_attack = "\nIts not very effective"
                    string_2_attack = "\nIts super effective"

                #Red is weak
                if Red.types == PokeType [(i+2)%3]:
                    self.attack *= 2
                    self.defense *= 2
                    Red.attack /= 2
                    Red.defense /= 2
                    string_1_attack = "\nIts super effective"
                    string_2_attack = "\nIts not very effective"

        #Fighting Loops
        #Loops while both Self and Red still have health
        while (self.bars > 0) and (Red.bars > 0):
            #print health
            print(f"\n\t\t{self.name}: HLTH\t{self.health}")
            print(f"\n\t\t{Red.name}: HTLH\t{Red.health}\n\n")

            #Turns to attack
            print(f"Go {self.name}!")
            for i, x in enumerate(self.moves):
                print(f"{i+1}.", x)
            index = int(input("pick a move: "))
            delay_print(f"\n{self.name} used {self.moves[index-1]}!")
            time.sleep(1)
            delay_print(string_1_attack)

            # Determine Damage
            Red.bars -= self.attack
            Red.health = ""

            #defense boost + bars
            for j in range(int(Red.bars+.1*Red.defense)):
                Red.health +="="
            
            time.sleep(1)

            print(f"\n{self.name}\t\tHTLH\t{self.health}")
            print(f"{Red.name}\t\tHTLH\t{Red.health}\n")
            time.sleep(.5)

            #Fainted?
            if Red.bars <=0:
                delay_print("\n..." + self.name + ' fainted!')
                break


            #Reds Turn

            print(f"Go {Red.name}!")
            for i, x in enumerate(Red.moves):
                print(f"{i+1}.", x)
            index = int(input('Pick a move: '))
            delay_print(f"\n{Red.name} used {Red.moves[index-1]}!") 
            time.sleep(1)
            delay_print(string_2_attack)   

            #reds damage determined
            self.bars -= Red.attack
            self.health = ""

            #health plus defense for Red
            for j in range(int(self.bars+.1*self.defense)):
                self.health += "="

            time.sleep(1)
            print(f"{Red.name}\t\tHTLH\t{self.health}")
            print(f"{self.name}\t\tHTLH\t{Red.health}\n")

            #Did your(self) pokemon faint?
            if self.bars<=0:
                delay_print("\n..." + self.name + ' fainted. ')
                break 

        money = np.random.choice(5000)
        delay_print(f"\n You Won ${money}.")

if __name__ == '__main__':
    pass
    #make pokemon

    Charizard = Pokemon('Charizard', 'Fire', ['Flamethrower', 'Fly', 'Blast Burn', 'Fire Punch'], {'ATTACK':12, 'DEFENSE': 8})
    Swampert = Pokemon('Swampert', 'Water', ['Water Gun', 'Water Gun', 'Hydro Pump', 'Dig'],{'ATTACK': 10, 'DEFENSE':10})
    Venusaur = Pokemon('Venusaur', 'Grass', ['Vine Wip', 'Razor Leaf', 'Earthquake', 'Frenzy Plant'],{'ATTACK':8, 'DEFENSE':12})

    Charmander = Pokemon('Charmander', 'Fire', ['Ember', 'Scratch', 'Tackle', 'Fire Punch'],{'ATTACK':4, 'DEFENSE':2})
    Mudkip = Pokemon('Mudkip', 'Water', ['Water Gun', 'Tackle', 'Sludge', 'Dig'],{'ATTACK': 3, 'DEFENSE':3})
    Bulbasaur = Pokemon('Bulbasaur', 'Grass', ['Vine Wip', 'Razor Leaf', 'Tackle', 'Leech Seed'],{'ATTACK':2, 'DEFENSE':4})

    Charmeleon = Pokemon('Charmeleon', 'Fire', ['Ember', 'Scratch', 'Flamethrower', 'Fire Punch'],{'ATTACK':6, 'DEFENSE':5})
    Marshtomp = Pokemon('Marshtomp', 'Water', ['Water Gun', 'Water Gun', 'Sludge', 'Dig'],{'ATTACK': 5, 'DEFENSE':5})
    Ivysaur = Pokemon('Ivysaur\t', 'Grass', ['Vine Wip', 'Razor Leaf', 'Bullet Seed', 'Leech Seed'],{'ATTACK':4, 'DEFENSE':6})


#Choose your pokemon
    Mudkip.fight(Charizard) 