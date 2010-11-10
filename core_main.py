from unit_data import *
import os
random.seed()

global attacker
nano_one = nanosuit_omega()
grunt = kpa_milita()
attacker = nano_one
target = grunt

while 1:
    while attacker.acp[0] >= 1:
        order = raw_input("do what?,shoot,change weapon,load,cock,lock and load:  ")
        if  order == "shoot":
            attk_print = attacker.equipt_weapon.shoot(target)
            for item in attk_print:
                for i  in item:
                    print i, # needed to print attk_print proply
            attk_print = []
        if  order == "change weapon":
            new_weapon = raw_input(("what weapon ?; ",  attacker.rifle1.name, ";  ", attacker.rifle2.name, ";    ", attacker.pistol1.name,":"))
            attacker.change_weapon(eval(new_weapon))
            print "equipt weapon is now ", attacker.equipt_weapon
            
        if (order == "cock") and (attacker.equipt_weapon.type == "crossbow"):
            attacker.equipt_weapon.cock(attacker)
            
        if (order == "load"):
            attacker.equipt_weapon.load(attacker)
            
        if (order == "lock and load"):
            attacker.equipt_weapon.lock_and_load(attacker)


    command = "junk"
    while (command !="n") and (command !="q") :
        command = raw_input('Quit or Next turn?:  ')
        if  (command !="n") and (command !="q") :
            print "invalid command"
    #allows user to quit the progarm
    if (command == "q") or (target.state == "dead"):
        break
    
    if command == "n":
        ##clears the screen
        #os.system("clear")
        continue
