import pylab as plt
import numpy as np

"""
This is assuming a few things that cannot be so easily calculated:
1; Initiative order was assumed to be (you, familiar, monster). 
    I just picked one cause i couldn't be asked to write that conditional into the code as well
2; On your first turn, you summon the undead
3; The monster starts each of its turns within the undead's aura
4; On subsequent turns, if the creature is poisoned, you cast mind sliver. 
    If it is not, you give your familiar an extra attack as your action
5; if the Creature is poisoned, the familiar uses the help action to give the undead spirit advantage on the first attack

"""
#########################
########Input here:######
#########################

Spell_save_DC=15
Spell_attack_modifier = 7
AC = 17
ConSave = 6
IntSave=3

#If you want to see the calculation for casting at 4th level, delete the first # infront of the lines 171, 176, this enables the second attack fo the undead spirit


#For inspiration, check the average stats here: https://docs.google.com/spreadsheets/d/10anA394CmxeLYTxuMYVnmmjiYLLedXfv6MBbpxEy2Kw/edit#gid=0
#credit to Platypusbill over on the ENWorld forums for the spreadsheet :) 





def diceroll(d):
    return np.random.randint(1, d+1)

def probBelow(z ,n):
    return np.sum([1 for ele in z if ele <n])/len(z)

def probAboveEq(z ,n):
    return np.sum([1 for ele in z if ele >=n])/len(z)

def mean(X):
    return np.sum(X)/len(X)

def stdev(X):
    X2 = [ele**2 for ele in X]
    return abs(mean(X2)-mean(X)**2)**0.5

class Monster:
    def __init__(self, CONsave, INTsave, AC, DC, SA, verbose = False):
        self.SA=SA
        self.AC = AC
        self.INTsave = INTsave
        self.CONsave = CONsave
        self.poisoned = False
        self.paralyzed = False
        self.round = 0
        self.poisonrounds = 0
        self.penalty = False
        self.DC=DC
        self.verbose = verbose
        
    def MindSliver(self):
        if self.INTsave+diceroll(20)<self.DC:
            self.penalty=True
            
    def GetPenalty(self):
        if self.penalty:
            self.penalty=False
            return diceroll(4)
        else:
            return 0
        
    def SaveAgainstPoison(self):
        if self.CONsave+diceroll(20)-self.GetPenalty()<self.DC:
            self.poisoned=True
            return True
        else:
            return False
            
    def SpriteAttack(self, adv=False):
        attackroll = diceroll(20)+6
        if adv:
            attackroll = max([diceroll(20), diceroll(20)])+6
        if attackroll>=self.AC:
            if self.verbose:
                print("Saving against Sprite poison")
            if self.SaveAgainstPoison():
                if self.verbose:
                    print("Poisoned by Sprite")
                self.poisonrounds=10
            else: 
                if self.verbose:
                    print("Not poisoned by Sprite")
            
                
    def Turn(self, Aura=True):
        if self.verbose:
            print("start monster turn")
        self.round=+1
        if self.verbose:
            print("round %i" % self.round)
        if self.poisoned and self.poisonrounds==0:
            if self.verbose:
                print(self.poisonrounds)
            self.poisoned=False
            if self.verbose:
                print("Monster shook the poisoned condition")
        if Aura:
            if self.verbose:
                print("Saving against Putrid Aura")
            if self.SaveAgainstPoison():
                if self.verbose:
                    print("Poisoned by Putrid Aura")
        else:
            if self.verbose:
                ("\t Save successfull")
            
        if self.paralyzed:
            if self.verbose:
                print("Monster cannot do anything, it's paralyzed")
            self.paralysed=False
            return 2
        elif self.poisoned:
            if self.verbose:
                print("Monster is poisoned")
            return 1
        else:
            if self.verbose:
                print("Monster is fine")
            return 0
        
    def PutridAttack(self, adv=False):
        attackroll = diceroll(20)+self.SA
        if adv:
            attackroll = max([diceroll(20), diceroll(20)])+self.SA
        if attackroll>=self.AC:
            if self.poisoned and self.CONsave+diceroll(20)-self.GetPenalty()<self.DC:
                self.paralyzed=True
                if self.verbose:
                    print("Paralyzed")
            elif self.poisoned:
                if self.verbose:
                    print("resisted paralysis")
        else:
            if self.verbose:
                print("Missed by putrid attack")
         
class Combat:
    def __init__(self):
        self.monster = Monster(ConSave, IntSave, AC, Spell_save_DC, Spell_attack_modifier) 
        self.round = 0
        self.conditions = []
        self.conditions.append(self.Round0())
        for i in range(1, 5):
            self.conditions.append(self.Round())
        
    def Round0(self):
        #player, undead, sprite, monster
        self.round=+1
        self.monster.PutridAttack()
        self.monster.SpriteAttack(True)
        return self.monster.Turn()
    def Round(self):
        self.round=+1
        if self.monster.poisoned:
            self.monster.MindSliver()
            self.monster.PutridAttack(True)
            #self.monster.PutridAttack()#activate for lvl 7+
            return self.monster.Turn()
        else: 
            self.monster.SpriteAttack()
            self.monster.PutridAttack()
            #self.monster.PutridAttack()#activate for lvl 7+
            self.monster.SpriteAttack()
            return self.monster.Turn()
    def EndCombat(self):
        return self.conditions
    
def GetConditions():
    combat = Combat()
    conditions = combat.EndCombat()
    return conditions

def MakeStats(conditions):
    c = np.array(conditions).transpose()
    print("\t Fine \t Poisoned \t Paralyzed")
    lines = []
    def sumnumber(arr, test):
        return np.sum([1 for ele in arr if ele==test])/len(arr)
    for i in range(len(c)):
            p=sumnumber(c[i], 2)
            r = [sumnumber(c[i], 0), sumnumber(c[i], 1)+p, p]
            lines.append("Round%i \t %.2f \t %.2f \t\t %.2f" %(i+1, *r))
    for line in lines:
        print(line)

conditions = [GetConditions() for ele in range(10000)]
MakeStats(conditions)
