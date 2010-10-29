#def load_gun(gun, loader):
#    if gun.loaded_ammo < 0:
#        gun.loaded_ammo = 0
#    if gun.spare_ammo > (gun.clip_size - gun.loaded_ammo):
#        gun.spare_ammo = gun.spare_ammo - (gun.clip_size - gun.loaded_ammo)
#        gun.loaded_ammo = gun.clip_size
#    elif gun.spare_ammo <= (gun.clip_size - gun.loaded_ammo):
#        gun.loaded_ammo = gun.loaded_ammo + gun.spare_ammo
#        gun.spare_ammo = 0
#    loader.acp[0] -= gun.load_time
    
def change_weapon(new_weapon, owner):
    global print_list 
    if (new_weapon != owner.equipt_weapon) and (owner.acp[0] >= 12):
       owner.equipt_weapon = new_weapon
       owner.acp[0]  -=  12 
    elif  owner.acp[0] < 12:
        print_list.apphend  ([owner.name, " has not got enogth action points to change weapons , only has ", owner.acp[0]])
def change_fire_mode( weapon,new_mode ):
    weapon.fire_mode = new_mode
    
