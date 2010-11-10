import random
####################################################################
###################################
##################
class over_heatable():
    
    
    heat_have = 0
    heat_gen = 5# amount of heat genarated by one shot
    cooling_rate = 5
    max_heat = 5 # maxium heat BEFORE weapon over heats
    over_heated = False
    def check_heat(self):
        if (self.heat_have > self.max_heat) and(self.over_heated == False):
            self.over_heated = True
            self.heat += (self.heat_gen*5)
            return self.name, " is over heated, wait for it to cool down before firig again"
            
    def cool_down(self):
        if self.heat_have >= self.cooling_rate:
           self.heat_have -= self.cooling_rate
        elif self.heat_have < self.cooling_rate:
            self.heat_have = 0
        if (self.heat_have <= (self.max_heat*0.75)) and (self.over_heated == True):
           self.over_heated = False 
##########################################################
class regen_ammo():
    
    max_ammo = 5
    available_ammo = 5
    regen_rate = 5
    def regenerate(self):
        if self.regen_rate <= (self.max_ammo - self.available_ammo):
            self.available_ammo += self.regen_rate
        elif self.regen_rate > (self.max_ammo - self.available_ammo):
            self.available_ammo = self.max_ammo
##############################################
################################
##########################################################################################################
class fire_arm():
    
    type = set(("fire arm"))
    max_ammo = 5 #maxium spare ammunition
    spare_ammo = 5 # avalible spare ammo
    clip_size = 5
    loaded_ammo = 5 # ammunition currantly in clip
    loaded = True
    load_time = 5 # amount of action point used to reload gun
    bursts = False 
    semi_firerate = 5
    accuracy = [5, 5, 5]#short range , medium range, long range
    burst_accuracy = [5, 5, 5]
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
        
    def load(self, loader):
        if self.loaded_ammo < 0:
            self.loaded_ammo = 0
        if self.spare_ammo > (self.clip_size - self.loaded_ammo):
            self.spare_ammo = self.spare_ammo - (self.clip_size - self.loaded_ammo)
            self.loaded_ammo = self.clip_size
        elif self.spare_ammo <= (self.clip_size - self.loaded_ammo):
            self.loaded_ammo = self.loaded_ammo + self.spare_ammo
            self.spare_ammo = 0
        loader.acp[0] -= self.load_time
        
    def change_fire_mode(self):
        if self.fire_mode == "auto":
            self.fire_mode = "semi"
        elif (self.fire_mode == "semi") and (self.bursts != False):#checks to see if the gun has auto fire ability
            self.fire_mode = "auto"
        else:
            print "this gun has not got mulitpile fire modes"

####################################################################
###################################
###########################

class crossbow():
    
  
    type = set("crossbow")
    name = "crossbow"
    max_bolts = 50
    spare_bolts = {"quarrels":20, "poisoned bolt":0, "tranquiliser dart":5}
    cocked = True
    loaded = True
    accuracy = [5, 5, 5]#short range , medium range, long range
    load_time = 5 #acp used to load bow
    cock_time = 5 #acp used to cock bow
    bolts_equipt = 'undfined'
    loaded_type = 'undfined' # type of bolt loaded
    bolt_options = set(("quarrel", "poisoned bolt", "tranquiliser dart"))
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
            return loader.name," does not have enougth action points"
    
    def load(self, loader):
        if (self.cocked == True) and (self.loaded == False) and (loader.acp[0] >= self.load_time) and (self.spare_bolts[self.bolts_equipt] >= 1):
            self.loaded = True
            loader.acp[0] -= self.load_time
            self.spare_bolts[self.bolts_equipt] -= 1
            self.loaded_type = self.bolts_equipt
            
        elif (self.cocked == True) and (self.loaded == True):
            return "crossbow already loaded"
            
        elif  loader.acp[0] < self.loadtime :
            return loader.name ,  " does not have enougth action points"
            
        elif self.spare_bolts[self.bolts_equipt] < 1:
            return loader.name," is out of ", self.bolts_equipt, "s, change equipt bolts"
        if self.cocked == False:
            return "cross bow not cocked, can not be loaded till it is cocked"
            
    def reload(self, loader):#change the type of bolt loaded once the crossbow has been loaded
        if self.loaded_type == bolts_equipt:
            return "crossbow it already loaded with a ", self.blot_loaded
        elif (self.cocked == True) and (self.loaded == True) and (loader.acp[0] >= self.load_time*2) and (self.spare_bolts[self.bolts_equipt] >= 1):
            loader.acp[0] -= (self.load_time*2) #twice as long bucuase it needas to be unloaded first
            self.spare_bolts[self.loaded_type] += 1
            self.spare_bolts[self.bolts_equipt] -= 1
            self.loaded_type = self.bolts_equipt
            
        elif  loader.acp[0] < (self.loadtime*2) :
            return loader.name ,  " does not have enougth action points"
        elif self.spare_bolts[self.bolts_equipt] < 1:
            return loader.name," is out of ", self.bolts_equipt, "s, change equipt bolts"
            
    def lock_and_load(self, loader):# cock it if not already cocked, and loads it 
        self.cock(loader)
        self.load(loader)
        
    def change_bolt_type(self, new_type):
        if (new_type in self.bolt_options) and (self.spare_bolts[self.newtype]):
            self.bolts_equipt = new_type
        elif new_type not in self.bolt_options:
            return new_type,"s are not valid bolts for this crossbow, valid types are:  ", self.bolt_options
        elif self.spare_bolts[new_type] < 1:
            return loader.name," is out of ", new_type, "s, change equipt bolts"
    
    def shoot(self, target):
        self.print_list=[]
        if self.loaded == True:
            #see if the attack hits
            if random.randint(1, 100) <= self.accuracy:
                #applying damage
                target.hp_have = target.hp_have - (self.loaded_type()*target.armour[1])
                self.print_list.append([ self.name," hits ",target.faction," now has " , target.hp_have, " hp remaining \n"]) 
            else:
                self.print_list.append([ self.name," missed \n"])    
            self.loaded = False
            self.cocked = False
        else :
            self.print_list.append(["blank"])
        if target.hp_have <= 0:
            target.state = "dead"
        return self.print_list
###################################################################################################################
#########################################################################
#################################################################
class ice_shard_projector(over_heatable, regen_ammo):
    type = set(("regen", "over_heatable", "shard projector"))
    accuracy = [5, 5, 5]#short range , medium range, long range
    bursts = 5
    
    heat_gen = 5# amount of heat genarated by one shot
    cooling_rate = 5
    max_heat = 5 # maxium heat BEFORE weapon over heats
    
    max_ammo = 5
    available_ammo = 5
    regen_rate = 5
    
    attachments = {}
    valid_attachments = set()
    range = {"short":5,"medium":5,  "long":5} 
    def damage(self):
        return random.randint(5, 6)
    
    def burst_size(self):
        return random.randint(5, 6)
        
    def shoot(self, target):
        global print_list
        print_list = []
        if (self.available_ammo >= self.burst_size()) and (self.over_heated == False):
            shots_remain = self.burst_size()
            
            while (shots_remain >= 1) and (target.state != "dead") and (self.over_heated == False):
                #see if the attack hits
                if random.randint(1, 100) <= self.accuracy :
                    #applying damage
                    target.hp_have = target.hp_have - (self.damage()*target.armour[1])
                    print_list.append([ self.name," hits ",target.faction," now has " , target.hp_have, " hp remaining \n"]) 
                else:
                    print_list.append([self.name," missed \n"])  
                '''reduces the amuont of left in this burst;;  reduces ammo in the gun;;  heats up the gun;;  checks to see if the is over heated'''
                shots_remain -= 1
                self.available_ammo -= 1
                self.heat_have += self.heat_gen
                self.check_heat()
                if self.over_heated == True:
                    print self.name, " is over heated, wait for it to cool down more"

        if self.available_ammo < self.burst_size():
            print self.name, " is out of ammunition, wait for it regenerate some more"
        self.cool_down()# 

###################################################################################################################
#########################################################################
#################################################################
class repeter_crossbow():
    
    max_ammo = {"quarrel":5,"posioned bolt": 5, "tranquiliser dart":5} #maxium spare ammunition
    spare_ammo = {"quarrel":5,"posioned bolt": 5, "tranquiliser dart":5} # avalible spare ammo
    clip_size = 5
    loaded_bolts = 5# number of bolts currently loaded
    loaded = True
    accuracy = 5
    repeat_rate = 5
    load_time = 5# amount of action points used to reload crossbow
    bolts_equipt = "quarrel"
    loaded_type = "qurrel" # type of bolts loaded
    bolt_options = set(("quarrel", "poisoned bolt", "tranquiliser dart"))
    range = {"short":5,"medium":5,  "long":5}
    sight_attachment = "iron sight"
    valid_sights = set(("scope", "iron sight", "rail sight"))
    def qurrel(self):
        return random.randint
        
    def load(self, loader):
        if (self.loaded_bolts < self.clip_size) and (loader.acp[0] >= self.load_time) and (self.spare_bolts[self.bolts_equipt] >= 1):
            self.loaded = True
            loader.acp[0] -= self.load_time
            self.spare_bolts[self.bolts_equipt] -=  (self.clip_size-self.loaded_bolts)
            self.loaded_type = self.bolts_equipt
            
        elif (self.loaded_bolts == self.clip_size) and (loaded == True):
            return "crossbow already loaded"
        elif  loader.acp[0] < self.loadtime :
            return loader.name ,  " does not have enougth action points"
        elif self.spare_bolts[self.bolts_equipt] < 1:
            return loader.name," is out of ", self.bolts_equipt, "s, change equipt bolts"
            
    def change_bolt_type(self, new_type):
        if (new_type in self.bolt_options) and (self.spare_bolts[self.newtype]):
            self.bolts_equipt = new_type
        elif new_type not in self.bolt_options:
            return new_type,"s are not valid bolts for this crossbow, valid types are:  ", self.bolt_options
        elif self.spare_bolts[new_type] < 1:
             return loader.name," is out of ", new_type, "s, change equipt bolts"
    
    def reload(self, loader):#change the type of bolt loaded once the crossbow has been loaded
        if self.loaded_type == bolts_equipt:
            return "crossbow it already loaded with ", self.blot_loaded, "s"
            
        elif (loaded == True) and (loader.acp[0] >= self.load_time) and (self.spare_bolts[self.bolts_equipt] >= 1):
            loader.acp[0] -= (self.load_time*2) #twice as long bucuase it needs to be unloaded first
            self.spare_bolts[self.loaded_type] += self.loaded_bolts
            loaded_bolts = 0
            self.load(loader)
            
        elif  loader.acp[0] < (self.loadtime*2) :
            return loader.name ,  " does not have enougth action points"
        elif self.spare_bolts[self.bolts_equipt] < 1:
            return loader.name," is out of ", self.bolts_equipt, "s, change equipt bolts"
    def shoot(self):
        print "this just to stop eric calling a bug,relpace with shooting code"
