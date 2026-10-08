import pygame
import numpy as np
import time

win=pygame.display.set_mode((900,800))
run=True

class Particle:
    def __init__(self):
        self.velocity=(0,0)
        self.position=(0,0)
        self.NetForce=(0,0)
        self.mass=10
        self.charge=1
    def motion(self,dt):
        acceleration=(np.array(self.NetForce)/self.mass).tolist()
        self.velocity=tuple(np.add(self.velocity,np.array(acceleration)*dt).tolist())
        self.position=tuple(np.add(self.position,np.array(self.velocity)*dt).tolist())
        if self.position[1]>=win.get_height():
            self.position=(self.position[0],win.get_height())
    def ApplyForce(self,f:tuple):
        self.NetForce=tuple(np.add(np.array(self.NetForce),np.array(f)).tolist())

    def render(self):
        pygame.draw.circle(win,(255,0,0),(self.position[0],self.position[1]),5)
    
a=Particle()
a.position=(0,250)
a.velocity=(20,0)
a.ApplyForce((0,0))
dt=0
clock=pygame.time.Clock()
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    win.fill((255,255,255))
    a.motion(dt)
    a.render()
    dt=clock.tick(60)/250
    pygame.display.update()
    
    

pygame.quit()