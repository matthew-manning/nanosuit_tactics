import random

#################################
####################
###################################################################
class fire_arm():
    max_ammo = 5 #maxium spare ammunition
    spare_ammo = 5 # avalible spare ammo
    clip_size = 5
    loaded_ammo = 5 # ammunition currantly in clip
    loaded = True
    load_time = 5
    bursts = 5 # number of bursts the gun can fire per turn
    semi_firerate = 5
    accurcy = 5
    burst_accuracy = 5
    fire_mode = "auto"# holds what fire mode the gun is in <"auto","semi","single">
    attachments = {}
    valid_attachments = set()
    range = {"short":5,"medium":5,  "long":5} 
    def burst_size(self):  
        return random.randint(5, 5) # the amount of bullets fired per burst
    def damage(self):
        return random.randint(5, 5)
        
    def shoot(self, target):
        #######################auto  fire
        global print_list
        print_list = []
        if (self.fire_mode == "auto") and (self.loaded_ammo >= self.burst_size()):
            shots_remain = self.burst_size()
            while (shots_remain >= 1) and (target.state != "dead"):
                #see if the attack hits
                if random.randint(1, 100) <= self.burst_accuracy :
                    #applying damage
                    damage_inf = self.damage()*target.armour[1]
                    target.hp_have = target.hp_have - (self.damage()*target.armour[1]/2)
                    print_list.append([ self.name," hits ",target.faction," now has " , target.hp_have, " hp remaining \n"]) 
                else:
                    print_list.append([self.name," missed \n"])  
                shots_remain -= 1
                self.loaded_ammo -= 1
                
        if (self.fire_mode == "single shot") and (self.loaded_ammo  >= 1):
            #see if the attack hits, single shot has more chance of hitting
            if random.randint(1, 100) <= self.accuracy:
                #applying damage
                target.hp_have = target.hp_have - (self.damage() *target.armour[1])
                print_list.append(["" , self.name," hits ",target.faction," now has " , target.hp_have, " hp remaining \n"]) 
            else:
                print_list.append(["" , self.name," missed \n"])    
            self.loaded_ammo -= 1
            
        if target.hp_have <= 0:
            target.state = "dead"
        return print_list
    def load_gun(self, loader):
        if self.loaded_ammo < 0:
            self.loaded_ammo = 0
        if self.spare_ammo > (self.clip_size - self.loaded_ammo):
            self.spare_ammo = self.spare_ammo - (self.clip_size - self.loaded_ammo)
            self.loaded_ammo = self.clip_size
        elif self.spare_ammo <= (self.clip_size - self.loaded_ammo):
            self.loaded_ammo = self.loaded_ammo + self.spare_ammo
            self.spare_ammo = 0
        loader.acp[0] -= self.load_time
    def change_fire_mode( self,new_mode ):
        self.fire_mode = new_mode
        self.fire_mode = new_mode
####################################################################
###################################
###########################

class crossbow():
    name = "crossbow"
    max_bolts = 50
    spare_bolts = {"quarrels":20, "poison bolt":0, "tranquiliser dart":5}
    cocked = True
    loaded = False
    accurcy = 5
    load_time = 5 #acp used to load bow
    cock_time = 5 #acp used to cock bow
    bolts_equipt = "quarrel"
    bolt_loaded = "qurrel" # type of bolt loaded
    bolt_options = set("quarrel", "poison bolt", "tranquiliser dart")
    range = {"short":5,"medium":5,  "long":5}
    sight_attachment = "iron sight"
    valid_sights = set(("scope", "iron sight", "rail sight"))
    
    def quarrel(self):
        return random.randint(5, 6)
    
    def cock(self, loader):
        if (self.cocked == False) and loader.acp[0] >= self.cock_time:
            self.cocked = True
            loader.acp[0] -= self.cock_time
            
        elif self.cocked == True:
            return "crossbow already cocked"
            
        elif loader.acp[0] < self.cock_time:
            return loader.name," does not have enogth action points"
    
    def load(self, loader):
        if (cocked == True) and (loaded == False) and (loader.acp[0] >= self.load_time) and (self.spare_bolts[self.bolts_equipt] >= 1):
            self.loaded = True
            loader.acp[0] -= self.load_time
            self.spare_bolts[self.bolts_equipt] -= 1
            self.bolt_loaded = self.bolts_equipt
            
        elif (cocked == True) and (loaded == True):
            return "crossbow already loaded"
            
        elif  loader.acp[0] < self.loadtime :
            return loader.name ,  " does not have enogth action points"
            
        elif self.spare_bolts[self.bolts_equipt] < 1:
            return loader.name," is out of ", self.bolts_equipt, "s, change equipt bolts"
        if self.cocked == False:
            return "cross bow not cocked, can not be loaded till it is cocked"
            
    def reload(self, loader):#change the type of bolt loaded once the crossbow has been loaded
        if self.bolt_loaded == bolts_equipt:
            return "crossbow it already loaded with a ", self.blot_loaded
            
        elif (cocked == True) and (loaded == True) and (loader.acp[0] >= self.load_time) and (self.spare_bolts[self.bolts_equipt] >= 1):
            loader.acp[0] -= (self.load_time*2) #twice as long bucuase it needas to be unloaded first
            self.spare_bolts[self.bolts_equipt] -= 1
            self.bolt_loaded = self.bolts_equipt
            
        elif  loader.acp[0] < (self.loadtime*2) :
            return loader.name ,  " does not have enogth action points"
            
        elif self.spare_bolts[self.bolts_equipt] < 1:
            return loader.name," is out of ", self.bolts_equipt, "s, change equipt bolts"
    
    def lock_and_load(self, loader):# cock it if not already cocked, and loads it 
        self.cock(loader)
        self.load(loader)
        
    def change_bolt_type(self, new_type):
        if new_type in self.bolt_options:
            self.bolts_equipt = new_type
            
        elif new_type not in self.bolt_options:
            return new_type,"s are not valid bolts for this crossbow, valid types are:  ", self.bolt_options
    
    def shoot(self, target):
        if self.loaded == True:
            #see if the attack hits, single shot has more chance of hitting
            if random.randint(1, 100) <= self.accuracy:
                #applying damage
                target.hp_have = target.hp_have - (eval(self.bolt_loaded()) *target.armour[1])
                print_list.append([ self.name," hits ",target.faction," now has " , target.hp_have, " hp remaining \n"]) 
            else:
                print_list.append([ self.name," missed \n"])    
            self.loaded = False
            self.cocked = False
            
        if target.hp_have <= 0:
            target.state = "dead"
        return print_list
