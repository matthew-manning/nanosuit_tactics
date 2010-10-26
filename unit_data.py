class nanosuit_omega():
    name = "undfined(nano user's name here)"
    hp = [100, (100)] # currant hp,(max hp)
    armour = ("composite", 0.90)# muitpile damage by second value before applying to health
    faction = "undfined" # owner's faction
    speed = 6 
    equip = {}
    rifle1 = gk36_rifle()
    rifle2 = False
    pistol1 = fcl_pistol()
    pistol2 = False
    equipt_weapon = rifle1
    melee = [2, 20, 85]#number of attacks , damage , accrucy
    suit_modes = {"stealth":"grade_1", "max_armour":"grade_2", "strength":"grade_2", "speed":"grade_1"}#grade_1 power is best
    active_mode = self.suit_modes["max_armour"]
    suit_energy = [200, (40)] #first is energy pool , second is energy recharge rate(per turn)
    
class gk36_rifle():# h&k g36 assault rife
    name = "gk36r special forces assult rifle"
    max_ammo = 300 #maxium spare ammunition
    spare_ammo = 300 # avalible spare ammo
    clip_size = 40 
    loaded_ammo = 40 # ammunition currantly in clip
    loaded = True
    damage = 20
    auto_firerate = 4
    accurcy = 85
    attachments = {}
    valid_attachments = set(("torch", "reflex sight", "iron sight", "teloscopic scope", "tactical attachment", "suppreser"))
    range = {"short":12,"medium":25,  "long":40} 
    
    
