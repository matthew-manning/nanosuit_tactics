import random
import os
from unit_data import *
random.seed()




def ranged_attack(attacker, target, fire_mode):
        
    if (fire_mode == "auto fire") and (loaded_ammo >= 3):
        shots_remain = attacker.equipt_weapon.auto_firerate
        os.system("clear")#clears screen
        while (shots_remain >= 1) and (target.state != "dead"):
            print_list = []
            #see if the attack hits
            if random.randint(10, 100) <= attacker.equipt_weapon.accurcy:
                #applying damage
                target.hp = target.hp - (attacker.equipt_weapon.damage * target.armour[1])
                print_list.append("\t" , attacker.equipt_weapon.name," hits ",target.faction," now has " , target.hp, " hp remaining")
            else:
                print_list.append("\t" , attacker.equipt_weapon.name," missed")    
            shots_remain = shots_remain - 1
            loaded_ammo = loaded_ammo - random.randint(1, 6)
            
            
    if (fire_mode == "single shot") and (loaded_ammo >= 1):
        os.system("clear")#clears screen
        print_list = []
        #see if the attack hits, single shot has more chance of hitting
        if random.randint(1, 100) <= attacker.equipt_weapon.accurcy:
            #applying damage
            target.hp = target.hp - (attacker.equipt_weapon.damage * target.armour[1])
            print_list.append("\t" , attacker.equipt_weapon.name," hits ",target.faction," now has " , target.hp, " hp remaining")
        else:
            print_list.append("\t" , attacker.equipt_weapon.name," missed")    
        loaded_ammo = loaded_ammo -1

    #ckeck if target is dead{HP <= 0}, if it is then it's state is changed to "dead"
    if target.hp <= 0:
        target.state = "dead"
    return print_list
    
    
    #__________________________________________________________________________________________________
    #_______________________________________________________________________________________________________________________________________________
    #______________________________________________________________________________________________________________________________________________________________________
    
    
    def melee_attack(attacker, target):
        
        attacks_remain = attacker.melee[0]
        os.system("clear")#clears screen
        while (attacks_remain >= 1) and (target.state != "dead"):
            print_list = []
            #see if the attack hits
            if random.randint(10, 100) <= attacker.melee[2]:
                #applying damage
                target.hp = target.hp - (attacker.melee[1] * target.armour[1])
                print_list.append("\t melee attack hits ",target.faction," now has " , target.hp, " hp remaining")
            else:
                print_list.append("\t missed")    
            attacks_remain = attacks_remain - 1
            
  
        #ckeck if target is dead{HP <= 0}, if it is then it's state is changed to "dead"
        if target.hp <= 0:
            target.state = "dead"
        return print_list

#_______________________________________________________________________________________________________________________________________________
#___________________________________________________________________________________________________________________________________________________________________________________________
#_________________________________________________________________
def load_gun(gun):
    if gun.spare_ammo >= (gun.clip_size - gun.loaded_ammo):
        gun.spare_ammo = gun.spare_ammo - (gun.clip_size - loaded_ammo)
        gun.loaded_ammo = gun.clip_size
    elif gun.spare_ammo <= (gun.clip_size - gun.loaded_ammo):
        gun.loaded_ammo = gun.loaded_ammo + gun.spare_ammo
        gun.spare_ammo = 0
