__author__ = 'Ashish'
"""
1. Create a inheritance tree with the followinhg structure
    1. BaseCharacter
      1. Non-Playable Chanracter (NPC)
         1. Friendly
         2. Enemy
      2. Playable Character
         1. Archer
         2. Green Lantern
         3. Butcher

2. add printName function all charachters have
3. add 'self.attackDamage =5 ' attr for all enemies
4. Create weapon class within same file
5. Have all PC characters  start with a weapon


                        | Base character |
                        ------------------



"""
class BaseCharacter(object):
    def printName(self,name):
        print(name)

class NPC(BaseCharacter):
    pass

class PC(BaseCharacter):
    def __init__(self):
        self.weapon = Weapon()

class Friendly(NPC):
    pass

class Enemy(NPC):
    def __init__(self):
        self.attackDamage =5

class Archer(PC):
    pass

class GreenLantern(PC):
    pass

class Butchur(PC):
    pass

class Weapon():
    pass


## ======================================
if __name__ == '__main__':
	enemy = Enemy()
	print (enemy.attackDamage)
	butcher = Butchur()
	print (butcher.weapon)