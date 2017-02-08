import random
class City: 
    shops = ["Weapon shop", "Potion shop"]
    name = None
    #description = None
    def __init__(self, name):    
        self.name = name

class PotionShop:
    def __init__(self):
        potion = None
        inpt = raw_input ("Welcome to the potion shop, what do you want to buy?\n1. Health Potion ($50)\n2. Mana Potion($50)\n3. Suicide potion($50)\n")

        if mainCharacter.money <50: 
            print "What! You don't have enough money! Cheapskate! you only have this much money:"
            print mainCharacter.money
            
        else:
            if inpt == "1":
                potion = Healthpotion()
            if inpt == "2":
                potion = Manapotion()
            if inpt == "3":
                potion = Suicidepotion() 
            inpt = raw_input ('would you like to know more or just buy?\n1.know more\n2.buy\n')
            if inpt == "1" or inpt == "know more" or inpt == "Know more":
                pass #add info later.
            if inpt == "2" or inpt == "Buy":
                mainCharacter.money = mainCharacter.money - 50
                mainCharacter.Inventory.Addtobag(potion)
                print "Thanks, come again!"

      
# 1. Classes need to be declared in the order in which they appear.
# ex, if we want to make a LongSword in the WeaponShop class,
# we have to put the LongSword class ABOVE the WeaponShop class
class WeaponShop:
    def __init__(self):
        weapon = None
        inpt = raw_input("Welcome to the weapon shop. What would you like to buy?\n1.Longsword($50)\n2.Bow and arrows($50)\n")
        if mainCharacter.money <50: 
            print "What! you don't have enough money! Cheapskate! You only have this much money:"
            print mainCharacter.money 
        else: 
            if inpt == "1":
                weapon = Longsword()
            if inpt == "2":
                weapon = Bow()
            inpt = raw_input ("would you still like to by this?\n1.yes\n2.no\n")
            if inpt == "1" or inpt == "yes":
                mainCharacter.money = mainCharacter.money - 50
                mainCharacter.Inventory.Addtobag(weapon)
                print "Thanks, come again!"
            if inpt == "2" or inpt == "no":
                pass 
 
class Manapotion:
    use = "increase damage by ten"
class Potion:
    def equip():
        mainCharacter.equip(self)
class Inventory:
    list = {}
    def Addtobag(self, item):
        #make sure >0spots
        self.list[id(item)] = item
    def Openbag(self):
        for key in self.list:
            print self.list[key] 

            print self.list[key].__class__.__name__ 


            
class Healthpotion:
    use = "increase health by 100"
class Suicidepotion:
    use = "KILLS!!!!!"
    
            
class Weapon:
    crit = 0
    name = "Nothing yet"
    damage = 0
               
    def equip():
        mainCharacter.equip(self)

class LongSword(Weapon):
    damage = 50
    crit = 10
    name = "Long Sword"

class Bow(Weapon):
    damage = 75
    crit = 1
    name = "Bow"

class Battle:
    def __init__(self):
        print "FIGHT!"
        inpt = raw_input ('what would you like to do:\n1.fight\n2.run\n')
        if inpt == "fight" or inpt == "1":
            list = []
            numen = random.randint(1, 2)
            index = 0
            while index < numen:
                enmy = random.randint(1, 2):
                if enmy == 1:
                    list.append(Barbarian())
                elif enmy == 2:
                    list.append(Zombie())
                    
            while len(list) > 0:
                inpt = raw_input ('1. attack\n2. use potion\n')
                if inpt == "1" or inpt == "attack":
                    index = 1
                    
                    for enemy in list:
                        print index
                        print enemy.__class__.__name__, enemy. health
                        index = index + 1
                    inpt = raw_input("What enemey(s) would your like to fight? Enter a number: ")
                    #make sure to create code line that checks the users input
                    try:
                        inpt = int(inpt)
                        mainCharacter.attack(list[inpt - 1])
                    except:
                        pass
                    
                    
                    for enemy in list:
                        if enemy.health <= 0:
                            list.remove(enemy)
                            mainCharacter.money = mainCharacter.money + 10
                            print "Enemy Defeated! You have gained 10 money to be greedy with. Just remember you are still poor!"
                    for enemy in list:
                        inpt = raw_input ('The %s is about to attack you. What would you like to do:\n1.dodge\n2.block\n'%enemy.name)
                        if inpt == "dodge" or inpt == "1":
                            if mainCharacter.dodge() == False:
                               enemy.attack(mainCharacter)

                        elif inpt == "block" or inpt == "2":
                            pass
                        else:
                            print "check your spelling!"
                        inpt = raw_input ('would you like to use a special move?')
                        if inpt == "yes":
                            inpt = raw_input('You can use:\n1.lightning shot (Best for knight)\n2.invincible claws and teeth (best for werewolf)\n3.magical super power (best for rogue)\n')
                            if inpt == "1":
                                mainCharacter.specialMove(zombie)
                            else:
                                print "You failed!"
                                continue
                        if inpt == "no":
                            break
                            print "too bad"
                            
                elif inpt == "2" or inpt == "use potion":
                    inpt = raw_input ('Which potion would you like to use:\n1.Health\n2.Mana\n3.Suicide\n')
                    ###KIND OF A BIG PROBLEM! When people choose what potion, they could cheat by saying they want a health potion when they don't have it,and then they would get to use it anyway!!!
                    if inpt == "1" or inpt == "health" or inpt == "Health":
                        mainCharacter.healthpotion = mainCharacter.healthpotion - 1
                        mainCharacter.health = mainCharacter.health + 100
                    if inpt == "2" or inpt == "mana" or inpt == "Mana":
                        mainCharacter.manapotion = mainCharacter.manapotion - 1
                        mainCharacter.damage = mainCharacter.damage + 10
                    if inpt == "3" or inpt == "suicide" or inpt == "Suicide":
                        mainCharacter.suicidepotion = mainCharacter.suicidepotion - 1
                        inpt = raw_input ('YOU DIED!!! Please close terminal and come back again to play more')
        elif inpt == "run" or inpt == "2":
            print "you ran away! Coward!!!"

class Enemy:
    health = 1
    damage = 1
    name = "Your name here"
    def attack(self, enemy):
        enemy.health = enemy.health - self.damage
        print "Your foe dealt %d damage" % self.damage
class Zombie(Enemy):
    health = 100
    damage = 5
    name = "Zombie"
    def __init__(self):
        print "ahhhhh, brains, yum!"
class Barbarian(Enemy):
    health = 200
    damage = 15
    name = "Barbarian"
    def __init__(self):
        print "Im gonna kill yah!!"
    
        
            
    

class Character:
    dodgeChance = 50
    blockChance = 50
    health = 100
    city = None
    money = 100
    weapon = None
    mana = 100 
    damage = 5
    Inventory = Inventory()
    def stash(self, item):
        self.Inventory.Addtobag(item)
    def dodge(self):
        if random.randint(1,6) >3:
            print "Successful dodge!"
            return True
        else:
            print "Unsuccesful dodge"
            return False
    def parry(self):
        if random.randint(1,6) >3:
            print "Successful parry!"
            return True
        else:
            print "Unsuccesful parry"
            return False
    def block(self):
        if random.randint(1,6) >3:
            print "Successful block!"
            return True
        else:
            print "Unsuccesful block"
            return False
    def attack(self, enemy):
        if self.weapon == None:
            enemy.health = enemy.health - self.damage
            print "you dealt %d damage" % self.damage
        else:
            enemy.health = enemy.health - self.weapon.damage
            print "you dealt %d weapon damage" % self.weapon.damage
    def setCity(self, city):
        self.city = city
    def getCity():
        print self.city.name 
    def equip(self, weapon):
        self.weapon = weapon
    #We want to to use this method to make sure our code works.
    #it should show off the weapon we bought OR
    #nothing at all
    def showOff(self):
        if self.weapon == None:
            print "Oh shoot, I don't even have a weapon!"
        else:
            print "Ha! Ha! Check out my cool"
            print self.weapon.name

        


class Devil(Character):
    name = "Devil"
    

class Knight(Character):
    name = "Piercer"
    def specialMove(self, enemy):
        if mainCharacter.mana <15:
            print "you don't have enough mana!"
            return
        else:
            mainCharacter.mana = mainCharacter.mana - 15
            print "you shoot lightning, as that is your power as a knight."
            if random.randint(1,6) >3:
                enemy.health = enemy.health - 200
                print "you dealt %d damage" % 200
            if random.randint(1,6) <3:
                print "you failed your special move!!!"

            

class Rogue(Character):
    name = "Altair"
 

class Werewolf(Character): 
    name = "Wolverine"
    
        
################GAME STARTS HERE################

mainCharacter = None
startingCity = City("Boston")
inpt = raw_input('type the number or word of the main character you choose :\n1. knight\n2. werewolf\n3. rogue\n')

if inpt == "knight" or inpt == "1" or inpt == "Knight":
    mainCharacter = Knight()
    print "you have choosen the path of the knight, the bravest of the trisquod. Green blob zombies are attacking Manhattan. Learn from master wizard. Fight the zombies, or Humanity will be destroyed. If you want to know how much health you have, type \'how much health do I have\' or \'what is my health\'. If you want to know how much money you have, type \'how much money do I have. \'"
if inpt == "Werewolf"or inpt == "werewolf" or inpt == "2":
    print "you have chosen the path of the werewolf, the strongest and most vicious of the trisquod. Green blob zombies are attacking Manhattan. Learn from master wizard. Fight the zombies, or Humanity will be destroyed.If you want to know how much health you have, type \'how much health do I have\' or \'what is my health\'. If you want to know how much money you have, type \'how much money do I have. \'"
    mainCharacter = Werewolf()
if inpt == "Rogue" or inpt == "rogue" or inpt == "3":
    mainCharacter = Rogue()
    print "you have chosen the path of the rogue, the most tactical and stealthy of the trisquod. Green blob zombies are attacking Manhattan. Learn from master wizard. Fight the zombies, or Humanity will be destroyed.If you want to know how much health you have, type \'how much health do I have\' or \'what is my health\'. If you want to know how much money you have, type \'how much money do I have. \'"
if inpt.lower() == "dev":
    mainCharacter = Dev()
    print "Welcome developer, you have selected a class designed for your personal use that is otherwise off limits for players."

mainCharacter.setCity(startingCity)



 
while True:
    inpt = raw_input ("Menu\n  1.go to\n  2.show off\n  3.fight\n  4.Inventory\n")    
    if inpt == "go to" or inpt == "1": 
        #print startingCity.shops
        inpt = raw_input ("Type your store name here (1.potion or 2.weapon): ")
        
        if inpt == "potion" or inpt == "potion shop" or inpt == "1":
            potionShop = PotionShop()    
        elif inpt == "weapon" or inpt == "weapon shop" or inpt == "2":
            weaponShop = WeaponShop()
    elif inpt == "show off" or inpt == "2": 
        mainCharacter.showOff()
    elif inpt == "fight" or inpt == "3":
        battle = Battle()
    elif inpt == "Inventory" or inpt == "4":
        mainCharacter.Inventory.Openbag()
    elif inpt == "what is my health?" or inpt == "what is my health" or inpt == "how much health do I have?" or inpt == "how much health do I have":
        print mainCharacter.health
    elif inpt == "how much money do I have?" or inpt == "how much money do I have":
        print mainCharacter.money
    elif inpt == "1" or inpt == "2" or inpt == "3" or inpt == "4" or inpt == "5" or inpt == "6" or inpt == "7" or inpt == "8" or inpt == "9":
        pass
    else:
        print "What's the matter with you, spell it right!!!"





#list of things that we want to do:
#1.break up the code into several files to make it easier to orginize
#2.turn potions into classes (class potion)
#3.give different classes special moves
#4.add sound effects
#5.create and actual story line  

