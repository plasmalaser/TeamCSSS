import pygame
import math
import Sound.soundlib
class Bullet():

    def __init__(self, origin_x, origin_y, aim_x, aim_y, new_owner):
        self.Pos_x = origin_x
        self.Pos_y = origin_y
        self.Origin_x = origin_x
        self.Origin_y = origin_y
        self.Aim_x = aim_x
        self.Aim_y = aim_y
        self.size = 2
        self.rect = pygame.Rect(self.Pos_x,self.Pos_y,self.size,self.size)
        self.speed = 10
        self.m = (self.Aim_y - self.Origin_y)/(self.Aim_x - self.Origin_x) if (self.Aim_x - self.Origin_x) != 0 else 0 
        self.HasHit = False
        self.char_bullet = new_owner# is true if it belongs to the main character, false otherwise
        Sound.soundlib.play_sound("Pistol_Shot_01.wav")

        # BULLETS SHOULD DISAPEAR AT THE EDGE OF THE SCREEN, ON ENEMY OR PLAYER HIT, WALL OR DOOR HIT

        # ADD AMMO and RELOAD, and ROTATING GUN SPRITE

    def update(self,tick,current_level,enemylist,char):
        self.move(tick,current_level,enemylist,char)
        self.rect = pygame.Rect(self.Pos_x,self.Pos_y,self.size,self.size)

    def get_y(self,x):
        y = self.m*(x - self.Origin_x) + self.Origin_y
        return x

    def get_x(self,y):
        x = (1/self.m)*(y - self.Origin_y) + self.Origin_x
        return y

    def move(self,tick,current_level,enemylist,char):
        self.Pos_y += (self.Aim_y - self.Origin_y)*(self.speed/(math.sqrt(math.pow(self.Aim_x - self.Origin_x, 2) + math.pow(self.Aim_y - self.Origin_y, 2))))
        self.Pos_x += (self.Aim_x - self.Origin_x)*(self.speed/(math.sqrt(math.pow(self.Aim_x - self.Origin_x, 2) + math.pow(self.Aim_y - self.Origin_y, 2))))
        
        gridpos_x = int((self.Pos_x)//30)
        gridpos_y = int((self.Pos_y)//30)
        
        current_room = current_level.get_current_room()
        
        if (gridpos_x >= 0 and gridpos_x <= 35 and gridpos_y >= 0 and gridpos_y <= 23):
            if ( int( current_room[gridpos_x][gridpos_y] ) in (-1, 1, 2, 4, 9, 12, 13, 15, 20, 21, 22)):
                self.HasHit = True
            elif ( int( current_room[gridpos_x][gridpos_y] ) == 14):
                self.HasHit = True
                current_room[gridpos_x][gridpos_y] = 0

    def draw(self,tick,screen):
        pygame.draw.rect(screen, [0,0,0], self.rect, 2)
