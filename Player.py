class Player:
    maxHp = 50
    hp = maxHp
    maxMp = 30
    mp = maxMp
    level = 0 #CHANGED TO TEST
    exp = 0 #CHANGED TO TEST
    maxExp = 100
    abilities = [("Heal", 10), ("Mega Punch",5)]
    

    def __init__(self,name):
        self.name = name

    def heal(self):
        print("")
        healAmount = int(self.maxHp * .20)
        if self.mp >= self.abilities[0][1]:
            print ("You healed for",(healAmount),"health!")
            self.hp += healAmount
            self.mp -= self.abilities[0][1]
            if self.hp > self.maxHp:
                self.hp = self.maxHp
        else:
            print ("Not enough MP!")

    def megaPunch(self,Enemy):
        print("")
        damage = int(self.maxHp * .15)
        if self.mp >= self.abilities[1][1]:
            print ("You used Mega Punch and dealt",damage,"points of damage!")
            self.mp -= self.abilities[1][1]
            Enemy.hp -= damage
            if Enemy.hp <= 0:
                Enemy.hp = 0
                print ("You defeated",Enemy.name + ".")
                self.gainEXP(Enemy)
                #battleWon() #MAKE THIS METHOD
        else:
            print ("Not enough MP!")

    def gainEXP(self,Enemy):
        print("")
        #TAKE EXP DROP
        self.exp += Enemy.expDrop
        print("You gained",Enemy.expDrop,"experience points.")
        #CHECK IF LEVELED UP
        if self.exp >= self.maxExp:
            self.level += 1
            self.exp = 0
            print("You leveled up. You are now level",self.level + ".")
            print("")
            self.maxExp += int(self.maxExp * .20)
            hpGain = int(self.maxHp * .20)
            print("You gained",hpGain,"HP.")
            self.maxHp += hpGain
            self.hp = self.maxHp
            mpGain = int(self.maxMp * .20)
            print("You gained",mpGain,"MP.")
            self.maxMp += mpGain
            self.mp = self.maxMp
            print("")
            print("Next level: " + str(self.exp) + "/" + str(self.maxExp) + " experience points.")
            if self.level == 5:
                newAb = ("Typhoon", 15)
                self.abilities.append(newAb)
                print("")
                print("You learned a new ability:",newAb[0],"| MP Cost:",newAb[1])
            elif self.level == 10:
                newAb = ("Cyclone", 20)
                self.abilities.append(newAb)
                print("")
                print("You learned a new ability:",newAb[0],"| MP Cost:",newAb[1])
            elif self.level == 15:
                newAb = ("Super Heal", 30)
                self.abilities.append(newAb)
                print("")
                print("You learned a new ability:",newAb[0],"| MP Cost:",newAb[1])
            elif self.level == 20:
                newAb = ("Sandstorm", 40)
                self.abilities.append(newAb)
                print("")
                print("You learned a new ability:",newAb[0],"| MP Cost:",newAb[1])
            elif self.level == 25:
                newAb = ("Ultima", 50)
                self.abilities.append(newAb)
                print("")
                print("You learned a new ability:",newAb[0],"| MP Cost:",newAb[1])
    
    def attack(self,Enemy):
        print("")
        damage = int (self.maxHp * .10)
        print ("You attacked the enemy and dealt",damage,"points of damage!")
        Enemy.hp -= damage
        if Enemy.hp <= 0:
            Enemy.hp = 0
            print ("You defeated ",Enemy.name + ".")
            self.gainEXP(Enemy)
            #battleWon() #MAKE THIS METHOD

    def displayAbilities(self,Enemy):
        print("")
        x = 1
        if self.level < 5:
            for i in range(2):
                print(str(x) + " " + self.abilities[i][0] + " | MP Cost:",self.abilities[i][1])
                x += 1
        elif self.level < 10:
            for i in range(3):
                print(str(x) + " " + self.abilities[i][0] + " | MP Cost:",self.abilities[i][1])
                x += 1
        elif self.level < 15:
            for i in range(4):
                print(str(x) + " " + self.abilities[i][0] + " | MP Cost:",self.abilities[i][1])
                x += 1
        elif self.level < 20:
            for i in range(5):
                print(str(x) + " " + self.abilities[i][0] + " | MP Cost:",self.abilities[i][1])
                x += 1
        else:
            for ab in abilities:
                print(str(x) + ") " + ab[0] + " | MP Cost:",i[1])
                x += 1
        while True:
            try:
                print("")
                choice = int(input("Choose the corresponding ability number: "))
                if choice == 1:
                    self.heal()
                elif choice == 2:
                    self.megaPunch(Enemy)
                '''elif choice == 3:
                    self.megaPunch(Enemy)
                elif choice == 4:
                    self.megaPunch(Enemy)
                elif choice == 5:
                    self.megaPunch(Enemy)
                elif choice == 6:
                    self.megaPunch(Enemy)'''
                break
            except ValueError:
                print("Invalid input. Please try again: ")
                continue                       
                
    def display(self):
        print("")
        print (self.name,": ",self.hp,"/",self.maxHp,"HP"," | ",self.mp,"/",self.maxMp,"MP")
        
    def combatOptions(self,Enemy):
        print("")
        while True:
            try:
                choice = int(input("Press 1 to attack and 2 to use an ability."))
                if choice == 1:
                    self.attack(Enemy)
                elif choice == 2:
                    self.displayAbilities(Enemy)
                break
            except ValueError:
                print("Incorrect input, try again.")
                continue







