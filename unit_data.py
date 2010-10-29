import random
random.seed()
from weapon_classs import *
    

class gk36_rifle(fire_arm):# h&k g36 assault rife
    name = "gk36r rifle"
    max_ammo = 300 #maxium spare ammunition
    spare_ammo = 200 # avalible spare ammo
    clip_size = 40 
    loaded_ammo = 40 # ammunition currantly in clip
    loaded = True
    load_time = 12
    bursts =  3 # number of bursts the gun can fire per turn
    semi_firerate = 7
    accuracy = 85
    burst_accuracy = 70
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
    accuracy = 80
    burst_accuracy = 70
    attachments = {"sight":"iron sight", "under slung":"none", "barrel atchment":"none"}
    valid_attachments = set(("torch", "reflex sight", "iron sight", "suppreser"))
    range = {"short":10,"medium":25,  "long":38} 
    def damage(self):
        return random.randint(12, 16)
    def burst_size(self):  
        return random.randint(3, 5) # the amount of bullets fired per burst
class light_crossbow():
    name = "light crossbow"
    max_bolts = {"quarrels":50, "poison bolt":25}
    spare_bolts = {"quarrels":18, "poison bolt":3}
    accurcy = 90
    load_time = 6 #acp used to load bow
    cock_time = 17 #acp used to cock bow
    bolts_equipt = "quarrel"
    bolt_loaded = "qurrel" # type of bolt loaded
    bolt_options = set("quarrel", "poison bolt")
    range = {"short":10,"medium":20,  "long":35}
    sight_attachment = "iron sight"
    valid_sights = set(("scope", "iron sight", "rail sight"))
    def quarrel(self):
        return random.randint(25, 50)

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
    

class nanosuit_omega():
    name = "undfined(nano user's name here)"
    hp_have = 100
    hp_max = 100
    armour = ("composite", 0.90)# muitpile damage by second value before applying to health
    faction = "undfined" # owner's faction
    state = "idle" #dead ,idle ,attacking , etc
    speed = [6, (6)]  #currant , max
    acp = [40, (40)] #actinpoints, use to perform action pick up weapons , shoot , etc
    equip = {}
    rifle1 = gk36_rifle()
    rifle2 = False
    pistol1 = gost_pistol()
    pistol2 = False
    equipt_weapon = rifle1
    melee = [2, 20, 85]#number of attacks , damage , accrucy
    suit_modes = {"stealth":"grade_1", "max_armour":"grade_2", "strength":"grade_2", "speed":"grade_1"}#grade_1 power is best
    active_mode = self.suit_modes["max_armour"] 
    suit_energy = [200, (40)] #first is energy pool , second is energy recharge rate(per turn)
    
    
class kpa_grunt():
    name = "undfined(grunt's name here)"
    hp_have = 80
    hp_max = 80
    armour = ("kevlar", 0.95)# muitpile damage by second value before applying to health
    faction = "kpa" # owner's faction
    state = "idle" #dead ,idle ,attacking , etc
    speed = [5, (5)]  #currant , max
    acp = [30, (30)] #actinpoints, use to perform action pick up weapons , shoot , etc
    melee = [2, 10, 85]#number of attacks , damage , accrucy
  
class kpa_anti_armour(kpa_grunt):
    
    equip = {}
    rifle1 =  False#rpg628v# rpg luncher
    rifle2 = jekt487_rifle()
    pistol1 = gost_pistol()
    pistol2 = False
    equipt_weapon = rifle1
    
class kpa_milita(kpa_grunt):
    
    equip = {}
    rifle1 =  light_crossbow()
    rifle2 = False
    pistol1 = gost_pistol()
    pistol2 = False
    equipt_weapon = rifle1
