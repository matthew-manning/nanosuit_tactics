import pygame


class clickable_button():
    
    
    avatar_clicked = False# is the the button been clicked on?
    
    def __init__(self, image, pos_x,pos_y):
        self.avatar = pygame.image.load(image)#button's image
        self.button_rect = self.avatar.get_rect()#pygame.Rect(pos_x,pos_y, size_x, size_y)
        self.button_rect.move_ip(pos_x, pos_y)
        self.pos_x = pos_x
        self.pos_y = pos_y
        
    def draw(self,display , cord_x, cord_y):#draw self.avatar at given x,y coordinates
        display.blit(self.image, [cord_x, cord_y])
        
    def draw_at_pos( self, display):#draws self.avatar at self.pos_x,self.pos_y
        display.blit(self.avatar, [self.pos_x, self.pos_y])
        
    def check_mouse(self, display):# cheacks to see if the mouse is over the button
        mouse_pos= pygame.mouse.get_pos()
        mouse_buttons = pygame.mouse.get_pressed()
        
        if self.button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(display, [255, 0, 0],self.button_rect, 5)
        
        if self.button_rect.collidepoint(mouse_pos) and mouse_buttons[0]:#if lmb clicks button
           self.avatar_clicked =True
        else :
           self.avatar_clicked = False

class graphic_str_generator():
    
    #######---<quake>----
    quake_one =     pygame.image.load("graphics/fonts/quake_one.png")
    quake_two =     pygame.image.load("graphics/fonts/quake_two.png")
    quake_three =   pygame.image.load("graphics/fonts/quake_three.png")
    quake_four =     pygame.image.load("graphics/fonts/quake_four.png")
    quake_five =      pygame.image.load("graphics/fonts/quake_five.png")
    quake_six =       pygame.image.load("graphics/fonts/quake_six.png")
    quake_seven =   pygame.image.load("graphics/fonts/quake_seven.png")
    quake_eight =    pygame.image.load("graphics/fonts/quake_eight.png")
    quake_nine =     pygame.image.load("graphics/fonts/quake_nine.png")
    quake_zero =    pygame.image.load("graphics/fonts/quake_zero.png")
    
    
    def display_str(self, in_string,display, pos_x, pos_y):
        
        self.spacing_count = 0
        self.display_list = []
        in_string = str(in_string)#make into string so for loop can itarate it
        #generates the string
        for numeral in in_string:
            
            if numeral == "1":
                self.display_list.append([self.quake_one, self.spacing_count])
            elif numeral == "2":
                self.display_list.append([self.quake_two, self.spacing_count])
            elif numeral == "3":
                self.display_list.append([self.quake_three, self.spacing_count])
            elif numeral == "4":
                self.display_list.append([self.quake_four, self.spacing_count])       
            elif numeral == "5":
                self.display_list.append([self.quake_five, self.spacing_count])
            elif numeral == "6":
                self.display_list.append([self.quake_six, self.spacing_count])
            elif numeral == "7":
                self.display_list.append([self.quake_seven, self.spacing_count])
            elif numeral == "8":
                self.display_list.append([self.quake_eight, self.spacing_count])       
            elif numeral == "9":
                self.display_list.append([self.quake_nine, self.spacing_count])
            elif numeral == "0":
                self.display_list.append([self.quake_zero, self.spacing_count])
            
            self.spacing_count += 35
        #displays the string
        for numeral in self.display_list:
            display.blit(numeral[0], [pos_x + numeral[1], pos_y])
  
  
class weapon_page():
    
    number_printer = graphic_str_generator()
    page_avatar = pygame.image.load("page_background.png")#page's image
    no_weapon_avatar = pygame.image.load("no_weapon_avatar.png")#used when no weapon is selected
    
    def __init__(self, pos_x,pos_y, entity_name):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.nano_suit = entity_name
        
        self.button_rifle_2 = clickable_button("graphics/buttons/button_rifle_2.png", 650,500)
        self.button_rifle_1 = clickable_button("graphics/buttons/button_rifle_1.png", 800,500)
        self.button_pistol_2 = clickable_button("graphics/buttons/button_pistol_2.png", 650,650)
        self.button_pistol_1 = clickable_button("graphics/buttons/button_pistol_1.png", 800,650)
        self.button_load = clickable_button("graphics/buttons/button_load.png", 100,650)
        self.button_fire_mode = clickable_button("graphics/buttons/button_fire_mode.png", 250,650)
        self.loaded_ammo_icon = pygame.image.load("graphics/weapons/loaded_ammo.png")
        self.button_list = [self.button_load, self.button_fire_mode, self.button_rifle_2, self.button_rifle_1 ,self.button_pistol_2 ,self.button_pistol_1 ]
     
        self.rifle_1 = self.nano_suit.rifle_1
        self.rifle_2 = self.nano_suit.rifle_2
        self.pistol_1 = self.nano_suit.pistol_1
        self.pistol_2 = self.nano_suit.pistol_2
        self.selected_weapon = self.rifle_1
    
    def display_page(self, display):
        display.blit(self.page_avatar, [self.pos_x, self.pos_y])
        
        if self.selected_weapon != False:
            display.blit(self.selected_weapon.avatar, [400, 150])
        elif self.selected_weapon == False:
            display.blit(self.no_weapon_avatar, [400, 150])
        
        for button in self.button_list:
            button.draw_at_pos(display)
            button.check_mouse(display)
        
###########################################################################################
        if (self.button_load.avatar_clicked == True) and (self.selected_weapon != False):
            self.selected_weapon.load(self.nano_suit)
            print self.selected_weapon.loaded_ammo, " rounds remaining"
            
        if (self.button_fire_mode.avatar_clicked == True) and (self.selected_weapon != False):
            self.selected_weapon.change_fire_mode()
            print self.selected_weapon.fire_mode, " fire mode engaged"
            
        if self.button_rifle_1.avatar_clicked == True:
                self.selected_weapon = self.rifle_1
        if self.button_rifle_2.avatar_clicked == True:
            self.selected_weapon = self.rifle_2
        if self.button_pistol_1.avatar_clicked == True:
            self.selected_weapon = self.pistol_1
        if self.button_pistol_2.avatar_clicked == True:
            self.selected_weapon = self.pistol_2
        
        if self.selected_weapon != False:
            display.blit(self.loaded_ammo_icon, [420, 680])
            self.number_printer.display_str( self.selected_weapon.loaded_ammo,display, 520, 695)#prints the weapon's remaining ammo
##################################################################################################



class nano_page():
    
    
    page_avatar = pygame.image.load("page_background.png")#page's image
    pos_y = 0
    pos_x = 0
    nano_armour_avatar = pygame.image.load("graphics/units/nanosuit_armour.png")
    nano_cloak_avatar = pygame.image.load("graphics/units/nanosuit_cloak.png")
    nano_strength_avatar = pygame.image.load("graphics/units/nanosuit_strength.png")
    
    
    button_armour = clickable_button("graphics/buttons/nano_button_armour.png", 550,650)
    button_strength = clickable_button("graphics/buttons/nano_button_strength.png", 300,650)
    button_cloak = clickable_button("graphics/buttons/nano_button_cloak.png", 425,650)
    button_list = [button_armour, button_strength, button_cloak]
    
    selected_mode = "max_armour"
    selected_mode_avatar = nano_armour_avatar
    
    def __init__(self, pos_x,pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
    
    def display_page(self, display):
        display.blit(self.page_avatar, [self.pos_x, self.pos_y])
        self.check_buttons(display)
        
        display.blit(self.selected_mode_avatar, [400, 150])
        
    def check_buttons(self, display):
        for button in self.button_list:
            button.draw_at_pos(display)
            button.check_mouse(display)
            
        if self.button_strength.avatar_clicked == True:
            self.selected_mode = "max_strength"
            self.selected_mode_avatar = self.nano_strength_avatar
            
        if self.button_cloak.avatar_clicked == True:
            self.selected_mode = "cloak"
            self.selected_mode_avatar = self.nano_cloak_avatar
        
        if self.button_armour.avatar_clicked == True:
            self.selected_mode = "max_armour"
            self.selected_mode_avatar = self.nano_armour_avatar
