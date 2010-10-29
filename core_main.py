from unit_data import *
#from misc_funtions import *
import os
random.seed()

nano_one = nanosuit_omega()
grunt = kpa_grunt()
attacker = nano_one
target = grunt


while 1:
    order = raw_input("do what?,shoot,etc:  ")
    if  order == "shoot":
        attk_print = attacker.equipt_weapon.shoot(target)
        for item in attk_print:
            for i  in item:
                print i, # needed to print attk_print proply
        attk_print = []

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
