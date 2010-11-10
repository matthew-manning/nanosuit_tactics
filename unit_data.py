import random
random.seed()
from weapon_classes import *
import pygame
    

class gk36_rifle(fire_arm):# h&k g36 assault rife
    avatar =  pygame.image.load("graphics/weapons/gk36_rifle.png")
    name = "gk36r rifle"
    max_ammo = 300 #maxium spare ammunition
    spare_ammo = 200 # avalible spare ammo
    clip_size = 40 
    loaded_ammo = 40 # ammunition currantly in clip
    loaded = True
    load_time = 12
    bursts =  3 # number of bursts the gun can fire per turn
    semi_firerate = 7
    accuracy = [85, 85, 75]#short range , medium range, long range
    burst_accuracy = [70, 65, 55]#short range , medium range, long range
    fire_mode = "auto"# holds what fire mode the gun is in; <"auto","semi","single">
    attachments = {"sight":"iron sight", "under slung":"none", "barrel atchment":"none"}
    valid_attachments = set(("torch", "reflex sight", "iron sight", "teloscopic scope", "tactical attachment", "suppreser"))
    range = {"short":12,"medium":25,  "long":40} 
    def damage(self):
        return random.randint(13, 18)
    def burst_size(self):  
        return random.randint(3, 5) # the amount of bullets fired per burst
   
class jekt487_rifle(fire_arm):# ak-74 assault rife
    name = "jekt-487 rifle"
    max_ammo = 270 #maxium spare ammunition
    spare_ammo = 150 # avalible spare ammo
    clip_size = 30 
    loaded_ammo = 30 # ammunition currantly in clip
    loaded = True
    load_time = 12
    semi_firerate = 3
    bursts = 3
    fire_mode = "auto"# holds what fire mode the gun is in; <"auto","semi","single">
    accuracy = [80, 75, 65]#short range , medium range, long range
    burst_accuracy = [70, 65, 55]#short range , medium range, long range
    attachments = {"sight":"iron sight", "under slung":"none", "barrel atchment":"none"}
    valid_attachments = set(("torch", "reflex sight", "iron sight", "suppreser"))
    range = {"short":10,"medium":25,  "long":38} 
    def damage(self):
        return random.randint(12, 16)
    def burst_size(self):  
        return random.randint(3, 5) # the amount of bullets fired per burst

class light_crossbow(crossbow):
    name = "light crossbow"
    max_bolts = {"quarrels":50, "poisoned bolt":25}
    spare_bolts = {"quarrels":18, "poisoned bolt":3}
    accuracy = [90, 85, 80]#short range , medium range, long range
    load_time = 6 #acp used to load bow
    cock_time = 17 #acp used to cock bow
    
    def quarrel(self):
        return random.randint(25, 50)
        
    bolts_equipt = "quarrel"
    loaded_type = quarrel # type of bolt loaded
    bolt_options = set(("quarrel", "poisoned bolt"))
    range = {"short":10,"medium":20,  "long":35}
    sight_attachment = "iron sight"
    valid_sights = set(("scope", "iron sight", "rail sight"))

class drav718_smg(fire_arm):# halo 2 smg
    name = "drav718_smg"
    max_ammo = 300 #maxium spare ammunition
    spare_ammo = 180 # avalible spare ammo
    clip_size = 60
    loaded_ammo = 60 # ammunition currantly in clip
    loaded = True
    load_time = 10
    semi_firerate = 4
    bursts = 2
    fire_mode = "auto"# holds what fire mode the gun is in; <"auto","semi","single">
    accuracy = 65
    burst_accuracy = 55
    attachments = {"sight":"iron sight", "under slung":"none", "barrel atchment":"none"}
    valid_attachments = set(("laser dot device","reflex sight", "iron sight", "suppreser"))
    range = {"short":5,"medium":12,  "long":18} 
    def damage(self):
        return random.randint(8, 12)
    def burst_size(self):  
        return random.randint(6, 10) # the amount of bullets fired per burst


class gost_pistol(fire_arm):#glock 17
    avatar =  pygame.image.load("graphics/weapons/gost_pistol.png")
    name = "gost 44mag pistol"
    max_ammo = 120 #maxium spare ammunition
    spare_ammo = 60 # avalible spare ammo
    clip_size = 17
    loaded_ammo = 17 # ammunition currantly in clip
    loaded = True
    load_time = 9
    semi_firerate = 2
    accuracy = 75
    fire_mode = "semi"# holds what fire mode the gun is in; <"auto","semi","single">
    attachments = {"sight":"iron sight", "under slung":"none", "barrel atchment":"none"}
    valid_attachments = set(( "reflex sight", "iron sight", "suppreser"))
    range = {"short":12,"medium":25,  "long":40} 
    def damage(self):
        return random.randint(16, 21)
############################################################
##################
##############################################################################################
###############################################################################################################
class human():
    name = "undfined"
    state = "idle" #dead ,idle ,attacking , etc
    faction = "undfined" # owner's faction
    condition = {"posioned":False, "frozen":False, "unconscious":False, "hallucination":False}
    resilience = 5
    def change_weapon(self, new_weapon):
        if (new_weapon != self.equipt_weapon) and (self.acp[0] >= 12):
            self.equipt_weapon = new_weapon
            self.acp[0]  -=  12 
        elif  self.acp[0] < 12:
            print  (self.name, " has not got enogth action points to change weapons , only has ", self.acp[0])
            
    def change_fire_mode( weapon,new_mode ):
        weapon.fire_mode = new_mode

class nanosuit_omega(human):
    resilience = 80
    hp_have = 100
    hp_max = 100
    armour = ("composite", 0.90)# muitpile damage by second value before applying to health
    speed = [8, (8)]  #currant , max
    acp = [40, (40)] #actinpoints, use to perform action pick up weapons , shoot , etc
    equip = {}
    rifle_1 = gk36_rifle()
    rifle_2 = False
    pistol_1 = gost_pistol()
    pistol_2 = False
    equipt_weapon = rifle_1
    melee = [2, 20, 85]#number of attacks , damage , accrucy
    suit_modes = {"stealth":"grade_1", "max_armour":"grade_2", "strength":"grade_2", "speed":"grade_1"}#grade_1 power is best
    active_mode = suit_modes["max_armour"] 
    suit_energy = [200, (40)] #first is energy pool , second is energy recharge rate(per turn)
    
    
class kpa_grunt(human):
    resilience = 30 + random.randint(5, 40)
    hp_have = 80
    hp_max = 80
    armour = ("kevlar", 0.95)# muitpile damage by second value before applying to health
    speed = [6, (6)]  #currant , max
    acp = [30, (30)] #actinpoints, use to perform action pick up weapons , shoot , etc
    melee = [2, 10, 85]#number of attacks , damage , accrucy
  
class kpa_anti_armour(kpa_grunt):
    
    equip = {}
    rifle_1 =  False#rpg628v# rpg luncher
    rifle_2 = jekt487_rifle()
    pistol_1 = gost_pistol()
    pistol_2 = False
    equipt_weapon = rifle_1
    
class kpa_milita(kpa_grunt):
    
    equip = {}
    rifle_1 =  light_crossbow()
    rifle_2 = False
    pistol_1 = gost_pistol()
    pistol_2 = False
    equipt_weapon = rifle_1
