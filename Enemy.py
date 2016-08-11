import sys

class Enemy:
    name = ""
    atk = 0
    hp = 0
    expDrop = 0
    
    def attack(self,Player):
        damage = self.atk
        print (self.name,"attacks for",damage,"points of damage!")
        Player.hp -= damage
        if Player.hp <=0:
            player.hp = 0
            print("YOU WERE DEFEATED! Game over.")
            sys.exit()

    def display(self):
        print (self.name,": ",int (self.hp),"/",self.maxHp,"HP")

class Zombie(Enemy):
    name = "Zombie"
    atk = 10
    hp = 25
    expDrop = 20
    maxHp = hp

class Ghost(Enemy):
    name = "Ghost"
    atk = 7
    hp = 30
    expDrop = 25
    maxHp = hp

class Boss(Enemy):
    name = "Zombie"
    atk = 15
    hp = 40
    expDrop = 50
    maxHp = hp
