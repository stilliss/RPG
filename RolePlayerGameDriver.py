import time
import sys

from Player import Player
from Enemy import *

#-----Combat Function-----#

def combat(Player,Enemy):
    while Player.hp > 0 and Enemy.hp > 0:
        Player.display()
        Enemy.display()
        Player.combatOptions(Enemy)
        if Enemy.hp > 0:
            Enemy.attack(Player)

#-----Combat Function-----#
'''
name = input("What is your name? ")

time.sleep(1)
print("*****PROLOGUE*****")
time.sleep(1)
print("Twenty years ago on the planet Gaia, there was a great war between the Pythonians and the Javians.")
time.sleep(1)
print("After many years of battle, the Javians finally claimed victory over the Pythonians.")
time.sleep(1)
print("After their defeat, all surviving Pythonians were exiled out of Gaia.")
time.sleep(1)
print("")
print("One of the small children spared by the Javians, ",name," has been preparing for a return. Now he has returned to Gaia for revenge.")
time.sleep(1)
print(name,"returns to his village where he makes a startling discovery...")
time.sleep(1)
print("Everything had been destroyed.")
time.sleep(1)
print("To make things worse, the area had been infested with monsters.")
time.sleep(1)
print("")
print("With the Javians' home base in mind, he set out to avenge his people.")
time.sleep(1)
print("")
print("A zombie approaches...")
time.sleep(3)
'''
player = Player("Seth")
zombie = Zombie()
ghost = Ghost()
boss1 = Boss()

time.sleep(1)

combat(player,zombie)

time.sleep(1)
print("You take a few more steps")

#TEST NEW COMBAT OPTIONS AND ATTACK METHODS
#CREATE BATTLEWON() METHODS
